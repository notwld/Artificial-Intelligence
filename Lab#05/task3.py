from queue import PriorityQueue

graph = {
    "A": ["B", "D"],
    "B": ["C", "E"],
    "C": [],
    "D": ["E", "H", "G"],
    "E": ["C", "F"],
    "F": [],
    "G": ["H"]
}

def greedy_best_first_search(graph, start):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    
    while not queue.empty():
        shush, node = queue.get()
        if node == "C":
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                h = len([n for n in graph[neighbor] if n != "C"])
                queue.put((h, neighbor))
    return False


if greedy_best_first_search(graph, "A"):
    print("A path to 'C' exists starting from node A.")
else:
    print("No path to 'C' exists starting from node A.")
