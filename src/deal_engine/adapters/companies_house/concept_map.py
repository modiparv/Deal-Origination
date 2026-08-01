"""Concept-map loader: (taxonomy namespace, local name, dimensions) ->
canonical concept.

The maps are versioned YAML data files, one per taxonomy family, living
with the adapter — the generic parse layer never contains registry
vocabulary. Unmapped names are reported, not silently dropped, so the
map grows from evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

_MAP_DIR = Path(__file__).parent / "concept_map"


@dataclass(frozen=True)
class DimensionalRule:
    dimension: str  # local name of the dimension, e.g. MaturitiesOrExpirationPeriodsDimension
    members: dict[str, str]  # member local name -> canonical concept


class ConceptMap:
    def __init__(
        self,
        direct: dict[tuple[str, str], str],
        dimensional: dict[tuple[str, str], DimensionalRule],
    ):
        self._direct = direct
        self._dimensional = dimensional

    @classmethod
    def load(cls, map_dir: Path = _MAP_DIR) -> "ConceptMap":
        direct: dict[tuple[str, str], str] = {}
        dimensional: dict[tuple[str, str], DimensionalRule] = {}
        for path in sorted(map_dir.glob("*.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            namespaces = data.get("namespaces", [])
            for local, canonical in (data.get("concepts") or {}).items():
                for ns in namespaces:
                    direct[(ns, local)] = canonical
            for local, rule in (data.get("dimensional_concepts") or {}).items():
                parsed = DimensionalRule(
                    dimension=rule["dimension"], members=dict(rule["members"])
                )
                for ns in namespaces:
                    dimensional[(ns, local)] = parsed
        return cls(direct, dimensional)

    def resolve(
        self, namespace: str, local_name: str, dimensions: dict[str, str]
    ) -> str | None:
        """Map a fact to a canonical concept, or None if unmapped.

        `dimensions` maps dimension local names to member local names
        (prefixes already stripped by the parser).
        """
        rule = self._dimensional.get((namespace, local_name))
        if rule is not None:
            member = dimensions.get(rule.dimension)
            return rule.members.get(member) if member else None
        return self._direct.get((namespace, local_name))
