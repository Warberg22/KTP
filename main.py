from typing import Dict, List, Tuple

# Knowledge base
# Each rule has: a name, an 'if' and a 'then'

Rule = Dict[str, Dict[str, int] | Dict[str, str] | str]


RULES: List[Rule] = [
    {
        "name": "NotFound_404",
        "if": {"status_code": 404},
        "then": {"diagnosis": "Endpoint not found (wrong path or route)."},
    },
    {
        "name": "ServerError_500",
        "if": {"status_code": 500},
        "then": {"diagnosis": "Internal server error (bug or failing dependency)."},
    },
    {
        "name": "Unauthorized_401",
        "if": {"status_code": 401},
        "then": {"diagnosis": "Unauthorized request (missing or invalid auth)."},
    },
]


# Inference engine (forward chaining, single pass)
def forward_chain(facts: Dict[str, int | str], rules: List[Rule]) -> Tuple[Dict[str, int | str], List[str]]:
    # small forward chaining: for each rile check all its 'if' conditions and match the current facts
    # if they match, add the 'then' facts to the fact base and return the final facts and a list of fired rule names
    fired: List[str] = []

    for rule in rules:
        conditions = rule["if"]
        if all(facts.get(key) == value for key, value in conditions.items()):
            then_part = rule["then"]
            for key, value in then_part.items():
                facts[key] = value
            fired.append(rule["name"])

    return facts, fired


# For now our UI is in the console, later we are thinking of using streamlit
def main() -> None:
    print("API Bug Diagnosis Assistant")
    print("This minimal prototype uses a few rules about HTTP status codes.\n")

    status_input = input("Choose one HTTP status code (i.e. 401, 404, 500): ")

    try:
        status_code = int(status_input)
    except ValueError:
        print("\nThis status code is not supported yet.")
        return

    # Initial facts
    facts: Dict[str, int | str] = {"status_code": status_code}

    # Run the inference step
    final_facts, fired_rules = forward_chain(facts, RULES)

    print("\n--- Facts after reasoning ---")
    for key, value in final_facts.items():
        print(f"{key}: {value}")

    print("\n--- Result ---")
    diagnosis = final_facts.get("diagnosis")
    if diagnosis:
        print("Diagnosis:", diagnosis)
    else:
        print("No diagnosis rule matched this status code.")

    print("\n--- Explanation (rules that fired) ---")
    if fired_rules:
        for name in fired_rules:
            print("-", name)
    else:
        print("No rules were triggered.")


if __name__ == "__main__":
    main()
