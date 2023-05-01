import heapq

def astar(graph, start, goal, heuristic):
    """
    Find the shortest path from start to goal in a weighted graph using A* search algorithm.

    :param graph: the weighted graph (dictionary of vertices and their edges with weights)
    :param start: the starting vertex
    :param goal: the goal vertex
    :param heuristic: the heuristic function (dictionary of estimated distances from each vertex to the goal)
    :return: the shortest path from start to goal
    """
    queue = [(0, [start])]
    visited = set()

    while queue:
        (cost, path) = heapq.heappop(queue)
        vertex = path[-1]

        if vertex == goal:
            return path

        if vertex in visited:
            continue

        visited.add(vertex)

        for (neighbor, edge_cost) in graph[vertex]:
            if neighbor not in visited:
                neighbor_cost = cost + edge_cost
                neighbor_heuristic = heuristic[neighbor]
                neighbor_f = neighbor_cost + neighbor_heuristic
                neighbor_path = path + [neighbor]
                heapq.heappush(queue, (neighbor_f, neighbor_path))

    return None

graph = {
    'Ar': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Ar', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Ar', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Ar', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]

}

h1 = {
    'Ar': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374

}

print(astar(graph, 'Ar', 'Bucharest', h1))



def a_star(graph, start, goal, heuristic):
    """
    A* algorithm implementation.

    :param graph: dictionary representing the graph
    :param start: starting node
    :param goal: goal node
    :param heuristic: function that takes two nodes and returns estimated cost between them
    :return: list of nodes representing the optimal path from start to goal
    """
    start_path = [start]
    cost = 0
    f = cost + heuristic(start, goal)
    queue = [(f, cost, start_path)]
    visited = set()

    while queue:
        f, cost, path = heapq.heappop(queue)
        current_node = path[-1]

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor, neighbor_cost in graph[current_node]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    new_cost = cost + neighbor_cost
                    f = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(queue, (f, new_cost, new_path))

    return None

def straight_line_distance(node, goal):
    h = h1[node] - h1[goal]
    return h

start_node = 'Ar'
goal_node = 'Bucharest'
path = a_star(graph, start_node, goal_node, straight_line_distance)
print(path)


