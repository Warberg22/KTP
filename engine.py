from typing import Dict, List, Tuple, Any
from kb import Rule


def forward_chain(facts: Dict[str, Any], rules: List[Rule]) -> Tuple[Dict[str, Any], List[str]]:
    # Forward chaining inference engine
    # Scans rules repeatedly and fires rules whose IF part matches the current facts
    # Adds/updates facts based on the THEN part
    # Stops when no more rules can fire
    fired: List[str] = []
    changed = True

    while changed:
        changed = False
        for rule in rules:
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
