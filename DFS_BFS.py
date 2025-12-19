
#bfs :
from collections import deque
from math import gcd

# Step 1: Check goal state
def is_goal(state, Z):
    return Z in state


# Step 2: Generate all possible next states
def get_next_states(state, X, Y):
    a, b = state
    return [
        (X, b),                                   # Fill Jug X
        (a, Y),                                   # Fill Jug Y
        (0, b),                                   # Empty Jug X
        (a, 0),                                   # Empty Jug Y
        (max(a - (Y - b), 0), min(Y, b + a)),     # Pour X -> Y
        (min(X, a + b), max(b - (X - a), 0))      # Pour Y -> X
    ]


# Step 3: BFS implementation
def bfs(X, Y, Z):
    queue = deque()
    visited = set()
    parent = {}

    start_state = (0, 0)
    queue.append(start_state)
    visited.add(start_state)
    parent[start_state] = None

    while queue:
        current = queue.popleft()

        if is_goal(current, Z):
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for state in get_next_states(current, X, Y):
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = current

    return None


# Step 4: Main function
if __name__ == "__main__":
    X = int(input("Enter capacity of Jug X: "))
    Y = int(input("Enter capacity of Jug Y: "))
    Z = int(input("Enter the target volume Z: "))

    if Z > max(X, Y):
        print("Target volume cannot be more than the capacity of the jugs.")
    elif Z % gcd(X, Y) != 0:
        print("No solution possible because Z is not divisible by GCD(X, Y).")
    else:
        result = bfs(X, Y, Z)

        if result:
            print("\nSteps to get", Z, "liters using BFS:")
            for step in result:
                print(step)
        else:
            print("No solution found.")


# Output:
# Enter capacity of Jug X: 5
# Enter capacity of Jug Y: 3
# Enter the target volume Z: 4

# Steps to get 4 liters using BFS:
# (0, 0)
# (5, 0)
# (2, 3)
# (2, 0)
# (0, 2)
# (5, 2)
# (4, 3)

#DFS: 
# Step 1: DFS implementation
def dfs(X, Y, Z, state, visited, path):
    if is_goal(state, Z):
        path.append(state)
        return True

    visited.add(state)
    path.append(state)

    for next_state in get_next_states(state, X, Y):
        if next_state not in visited:
            if dfs(X, Y, Z, next_state, visited, path):
                return True

    path.pop()
    return False


# Step 2: Main DFS execution
if __name__ == "__main__":
    X = int(input("Enter capacity of Jug X: "))
    Y = int(input("Enter capacity of Jug Y: "))
    Z = int(input("Enter the target volume Z: "))

    visited = set()
    path = []

    if dfs(X, Y, Z, (0, 0), visited, path):
        print("\nSteps to get", Z, "liters using DFS:")
        for step in path:
            print(step)
    else:
        print("No solution found.")


# Algorithm (Common for BFS & DFS)

# Start with both jugs empty (0, 0)

# Generate all possible next states:

# Fill Jug X

# Fill Jug Y

# Empty Jug X

# Empty Jug Y

# Pour water from X → Y

# Pour water from Y → X

# Stop when either jug contains Z liters

# Use BFS for shortest path and DFS for depth traversal

