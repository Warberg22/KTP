from typing import Dict, List, Tuple, Any
from kb import Rule


def forward_chain(facts: Dict[str, Any], rules: List[Rule]) -> Tuple[Dict[str, Any], List[str]]:
    fired: List[str] = []
    changed = True

    PROTECTED_KEYS = {"category", "cause", "diagnosis", "recommendation"}

    # sort rules by number of conditions and priority
    sorted_rules = sorted(
        rules,
        key=lambda r: (len(r.get("if", {})), r.get("priority", 0)),
        reverse=True,
    )

    while changed:
        changed = False

        for rule in sorted_rules:
            name = rule.get("name", "<unnamed>")
            if name in fired:
                continue

            conditions = rule.get("if", {})
            if all(facts.get(key) == value for key, value in conditions.items()):
                then_part = rule.get("then", {})
                updated = False

                for key, value in then_part.items():
                    # Do not overwrite protected keys once set
                    if key in PROTECTED_KEYS and key in facts and facts.get(key) != value:
                        continue

                    if facts.get(key) != value:
                        facts[key] = value
                        updated = True

                fired.append(name)

                if updated:
                    changed = True

    return facts, fired
