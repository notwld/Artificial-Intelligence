from queue import Queue

class EightQ:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def get_successors(self, state):
        successors = []
        row, col = self.find_blank(state)

        if row > 0:
            successor = [row[:] for row in state]
            successor[row][col], successor[row-1][col] = successor[row-1][col], successor[row][col]
            successors.append(successor)

        if row < 2:
            successor = [row[:] for row in state]
            successor[row][col], successor[row+1][col] = successor[row+1][col], successor[row][col]
            successors.append(successor)

        if col > 0:
            successor = [row[:] for row in state]
            successor[row][col], successor[row][col-1] = successor[row][col-1], successor[row][col]
            successors.append(successor)

        if col < 2:
            successor = [row[:] for row in state]
            successor[row][col], successor[row][col+1] = successor[row][col+1], successor[row][col]
            successors.append(successor)

        return successors

    def find_blank(self, state):
        for row in range(3):
            for col in range(3):
                if state[row][col] == 0:
                    return row, col

    def perform_bfs(self):
        visited = set()
        queue = Queue()
        queue.put(self.initial_state)

        while not queue.empty():
            state = queue.get()

            if state == self.goal_state:
                return state

            visited.add(tuple(map(tuple, state)))

            successors = self.get_successors(state)
            for successor in successors:
                if tuple(map(tuple, successor)) not in visited:
                    queue.put(successor)

        return None


initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [6, 7, 8]]

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

puzzle = EightQ(initial_state, goal_state)
solution = puzzle.perform_bfs()

if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
