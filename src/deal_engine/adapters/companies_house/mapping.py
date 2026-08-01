"""Companies House JSON → canonical vocabulary.

The VOCABULARY translation, executed: registry-native field names come
in, neutral canonical fields go out as plain dicts ready for the
canonical models/tables. Identifiers are deterministic so re-ingest is
naturally idempotent.

Field realities honoured here (live-verified): officers carry
`person_number` (person identity) and month/year `date_of_birth`;
beneficial-owner records expose their registry id only in `links.self`;
pre-2013 charges have no `charge_code` (fall back to the number);
per-filing accounts regime is encoded in the filing description
(`accounts-with-accounts-type-<regime>`); `links.document_metadata` is
an absolute URL whose tail is the document id.
"""

from __future__ import annotations

JURISDICTION = "GB"
ADAPTER = "companies_house"


def company_id(registration_id: str) -> str:
    return f"gb:{registration_id}"


def map_company(profile: dict) -> dict:
    registration_id = profile["company_number"]
    return {
        "id": company_id(registration_id),
        "jurisdiction": JURISDICTION,
        "registration_id": registration_id,
        "name": profile.get("company_name", ""),
        "name_variants": [
            p.get("name") for p in profile.get("previous_company_names", []) if p.get("name")
        ],
        "incorporation_date": profile.get("date_of_creation"),
        "status": profile.get("company_status"),
        "classification_codes": list(profile.get("sic_codes", [])),
        "classification_taxonomy": "sic_2007",
        "registered_address": {
            k: str(v)
            for k, v in (profile.get("registered_office_address") or {}).items()
        },
    }


def map_officer(item: dict, cid: str) -> dict:
    person = str(item.get("person_number") or item.get("links", {}).get("officer", {}).get("appointments", "unknown")).rstrip("/").rsplit("/", 1)[-1]
    appointment = f"{person}:{item.get('appointed_on') or 'na'}"
    dob = item.get("date_of_birth") or {}
    return {
        "id": f"{cid}:officer:{appointment}",
        "company_id": cid,
        "appointment_id": appointment,
        "officer_id": person,
        "name": item.get("name", ""),
        "role": item.get("officer_role", ""),
        "appointed_on": item.get("appointed_on"),
        "resigned_on": item.get("resigned_on"),
        "dob_month": dob.get("month"),
        "dob_year": dob.get("year"),
        "nationality": item.get("nationality"),
        "country_of_residence": item.get("country_of_residence"),
    }


def map_beneficial_owner(item: dict, cid: str) -> dict:
    external = str(item.get("links", {}).get("self", "")).rstrip("/").rsplit("/", 1)[-1] or "unknown"
    dob = item.get("date_of_birth") or {}
    return {
        "id": f"{cid}:bo:{external}",
        "company_id": cid,
        "external_id": external,
        "kind": item.get("kind", ""),
        "name": item.get("name"),
        "name_elements": {
            k: str(v) for k, v in (item.get("name_elements") or {}).items()
        },
        "control_natures": list(item.get("natures_of_control", [])),
        "notified_on": item.get("notified_on"),
        "ceased_on": item.get("ceased_on"),
        "dob_month": dob.get("month"),
        "dob_year": dob.get("year"),
        "identification": {
            k: str(v) for k, v in (item.get("identification") or {}).items()
        },
    }


def account_type_from_description(description: str | None) -> str | None:
    prefix = "accounts-with-accounts-type-"
    if description and description.startswith(prefix):
        return description[len(prefix):]
    return None


def document_id_from_metadata_url(url: str | None) -> str | None:
    if not url:
        return None
    return url.rstrip("/").rsplit("/", 1)[-1]


def map_filing(item: dict, cid: str) -> dict:
    transaction = item.get("transaction_id", "")
    return {
        "id": f"{cid}:filing:{transaction}",
        "company_id": cid,
        "transaction_id": transaction,
        "category": item.get("category"),
        "subcategory": item.get("subcategory"),
        "type": item.get("type"),
        "filing_date": item.get("date"),
        "description": item.get("description"),
        "description_values": {
            k: str(v) for k, v in (item.get("description_values") or {}).items()
        },
        "document_id": document_id_from_metadata_url(
            item.get("links", {}).get("document_metadata")
        ),
        "paper_filed": item.get("paper_filed"),
    }


def map_ownership_statement(item: dict, cid: str) -> dict:
    external = str(item.get("links", {}).get("self", "")).rstrip("/").rsplit("/", 1)[-1] or "unknown"
    return {
        "id": f"{cid}:stmt:{external}",
        "company_id": cid,
        "statement": item.get("statement", ""),
        "notified_on": item.get("notified_on"),
        "ceased_on": item.get("ceased_on"),
    }


def map_exemptions(payload: dict | None, cid: str) -> list[dict]:
    # Live shape: {"exemptions": {<snake_key>: {items, exemption_type}}}.
    out: list[dict] = []
    for key, entry in ((payload or {}).get("exemptions") or {}).items():
        out.append(
            {
                "id": f"{cid}:exemption:{key}",
                "company_id": cid,
                "exemption_type": entry.get("exemption_type") or key,
                "items": [
                    {k: str(v) for k, v in item.items()}
                    for item in entry.get("items", [])
                ],
            }
        )
    return out


def map_security_interest(item: dict, cid: str) -> dict:
    external = item.get("charge_code") or f"num-{item.get('charge_number', 'unknown')}"
    return {
        "id": f"{cid}:security:{external}",
        "company_id": cid,
        "external_id": str(external),
        "status": item.get("status"),
        "created_on": item.get("created_on"),
        "delivered_on": item.get("delivered_on"),
        "satisfied_on": item.get("satisfied_on"),
        "classification": dict(item.get("classification") or {}),
        "details": dict(item.get("particulars") or {}),
        "secured_parties": [
            p.get("name") for p in item.get("persons_entitled", []) if p.get("name")
        ],
        "transactions": list(item.get("transactions", [])),
    }
