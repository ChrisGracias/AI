from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 3)
                goal_row, goal_col = divmod(state[i][j] - 1, 3)  # Correction: Use integer division (//)
                distance += abs(row - goal_row) + abs(col - goal_col)  # Correction: Use absolute difference
    return distance

# Define the possible moves
def possible_moves(state):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for dx, dy in directions:
                    new_x, new_y = i + dx, j + dy
                    if 0 <= new_x < 3 and 0 <= new_y < 3:
                        new_state = [row[:] for row in state]
                        new_state[i][j], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[i][j]
                        moves.append((new_state, (new_x, new_y)))
    return moves

# Solve the puzzle using A* algorithm
def solve_puzzle(initial_state):
    open_set = PriorityQueue()
    open_set.put((manhattan_distance(initial_state), 0, initial_state, []))
    closed_set = set()

    while not open_set.empty():
        _, cost, current_state, path = open_set.get()
        if current_state == goal_state:
            return path

        closed_set.add(tuple(map(tuple, map(tuple, current_state))))  # Correction: Convert to tuple of tuples

        for move_state, move in possible_moves(current_state):
            if tuple(map(tuple, move_state)) not in closed_set:
                new_cost = cost + 1
                new_path = path + [move]
                open_set.put((new_cost + manhattan_distance(move_state), new_cost, move_state, new_path))

    return None

# Print the solution path
def print_solution(path):
    if path is None:
        print("No solution found.")
        return
    
    for i, move in enumerate(path):
        print(f"Step {i + 1}: Move {move} to position {move[1]}")
        if isinstance(move[0], int):
            print("Invalid move")
        else:
            for row in move[0]:
                print(" ".join(str(cell) for cell in row))
        print()


# Example usage:
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
path = solve_puzzle(initial_state)
if path:
    print("Solution found:")
    print_solution(path)
else:
    print("No solution found.")
