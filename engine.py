from typing import Dict, List, Tuple, Any
from kb import Rule


def forward_chain(facts: Dict[str, Any], rules: List[Rule]) -> Tuple[Dict[str, Any], List[str]]:
    fired: List[str] = []

    # Sort rules by specificity
    sorted_rules = sorted(rules, key=lambda r: len(r["if"]), reverse=True)

    matched_specific = False

    for rule in sorted_rules:
        conditions = rule["if"]
        if all(facts.get(key) == value for key, value in conditions.items()):
            # Checks if it's a generic rule
            is_generic = len(conditions) == 1 and "status_code" in conditions

            if is_generic and matched_specific:
                continue  # skip generic rule if a specific one already matched

            for key, value in rule["then"].items():
                facts[key] = value

            fired.append(rule["name"])

            if not is_generic:
                matched_specific = True

    return facts, fired

