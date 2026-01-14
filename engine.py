from typing import Dict, List, Tuple, Any
from kb import Rule


def forward_chain(facts: Dict[str, Any], rules: List[Rule]) -> Tuple[Dict[str, Any], List[str]]:
    fired: List[str] = []
    changed = True

    # Sort rules by specificity (more conditions first)
    sorted_rules = sorted(rules, key=lambda r: len(r["if"]), reverse=True)

    while changed:
        changed = False

        for rule in sorted_rules:
            if rule["name"] in fired:
                continue

            conditions = rule["if"]

            if all(facts.get(key) == value for key, value in conditions.items()):
                then_part = rule["then"]
                updated = False

                for key, value in then_part.items():
                    if facts.get(key) != value:
                        facts[key] = value
                        updated = True

                fired.append(rule["name"])

                if updated:
                    changed = True

    return facts, fired
