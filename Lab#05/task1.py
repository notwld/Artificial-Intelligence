def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    print("Start -> ",start)
    while stack:
        node = stack.pop()
        print("Visted -> ",graph[node])

        if node == goal:
            print("Goal -> ",goal)
            return True

        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return False

graph = {
    "A": ["B", "D"],
    "B": ["C", "E"],
    "C": [],
    "D": ["E", "H", "G"],
    "E": ["C", "F"],
    "F": [],
    "G": ["H"]
}

print(dfs(graph, "A", "G"))
