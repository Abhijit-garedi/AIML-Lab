# Sample knowledge base
rules = [
    {"if": ["A"], "then": "B"},
    {"if": ["B"], "then": "C"},
    {"if": ["C"], "then": "D"},
    {"if": ["A", "E"], "then": "F"},
    {"if": ["F"], "then": "G"}
]



initial_facts = {"A", "E"}



# Forward Chaining implementation
def forward_chaining(rules, facts):


    inferred = set()
    changed = True

    print("\nForward Chaining Trace:")



    while changed:
        changed = False

        for rule in rules:
            if rule["then"] not in facts and all(
                cond in facts for cond in rule["if"]
            ):
                facts.add(rule["then"])
                inferred.add(rule["then"])

                print(f"Inferred {rule['then']} using {rule['if']}")
                changed = True



    return inferred



# Backward Chaining implementation
def backward_chaining(rules, facts, goal, visited=None):


    if visited is None:
        visited = set()



    if goal in facts:
        return True



    if goal in visited:
        return False

    visited.add(goal)



    for rule in rules:
        if rule["then"] == goal:
            if all(
                backward_chaining(rules, facts, cond, visited)
                for cond in rule["if"]
            ):
                facts.add(goal)   # cache inference
                print(f"Derived {goal} using {rule['if']}")
                return True



    return False



# Main execution
if __name__ == "__main__":

    print("Initial Facts:", initial_facts)



    # Forward chaining
    derived_facts = forward_chaining(rules, set(initial_facts))
    print("All inferred facts:", initial_facts.union(derived_facts))



    # Backward chaining
    goal = input(
        "\nEnter a goal to prove using Backward Chaining: "
    ).strip().upper()



    if backward_chaining(rules, set(initial_facts), goal):
        print(f"Goal '{goal}' can be proven.")
    else:
        print(f"Goal '{goal}' cannot be proven.")



"""
Output:

Initial Facts: {'A', 'E'}

Forward Chaining Trace:
Inferred B using ['A']
Inferred C using ['B']
Inferred D using ['C']
Inferred F using ['A', 'E']
Inferred G using ['F']

All inferred facts: {'G', 'D', 'F', 'C', 'E', 'B', 'A'}

Enter a goal to prove using Backward Chaining: c
Derived B using ['A']
Derived C using ['B']
Goal 'C' can be proven.
"""
