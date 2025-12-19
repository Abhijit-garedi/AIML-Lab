import heapq



def a_star(graph, start, goal, heuristics):


    # Priority queue elements: (f, g, current_node, path)
    queue = [(heuristics[start], 0, start, [start])]
    visited = set()



    while queue:
        f, g, current, path = heapq.heappop(queue)



        if current == goal:
            print("Shortest path:", " -> ".join(path))
            print("Total cost:", g)
            return



        if current in visited:
            continue

        visited.add(current)



        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )



    print("No path found!")



# Sample weighted graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 5, 'E': 12},
    'C': {'F': 2},
    'D': {'G': 3},
    'E': {'G': 2},
    'F': {'G': 3},
    'G': {}
}



# Heuristic values for each node
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}



# Get input from user
start_node = input("Enter start node: ").upper()
goal_node = input("Enter goal node: ").upper()



# Run A* algorithm
a_star(graph, start_node, goal_node, heuristics)



"""
Output:

Enter start node: a
Enter goal node: g
Shortest path: A -> B -> D -> G
Total cost: 9
"""
