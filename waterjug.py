from collections import deque

# Action functions
def fill_jug1(state):
    return (jug1_capacity, state[1])

def fill_jug2(state):
    return (state[0], jug2_capacity)

def empty_jug1(state):
    return (0, state[1])

def empty_jug2(state):
    return (state[0], 0)

def pour_jug1_to_jug2(state):
    amount_to_pour = min(state[0], jug2_capacity - state[1])
    return (state[0] - amount_to_pour, state[1] + amount_to_pour)

def pour_jug2_to_jug1(state):
    amount_to_pour = min(state[1], jug1_capacity - state[0])
    return (state[0] + amount_to_pour, state[1] - amount_to_pour)

# Breadth-first search function
def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        if state in visited:
            continue
        visited.add(state)
        for action_name, action_func in actions.items():
            next_state = action_func(state)
            if next_state not in visited:
                queue.append((next_state, path + [action_name]))
    return None

# Define capacities of jugs
jug1_capacity = 4
jug2_capacity = 3

# Actions dictionary
actions = {
    'fill_jug1': fill_jug1,
    'fill_jug2': fill_jug2,
    'empty_jug1': empty_jug1,
    'empty_jug2': empty_jug2,
    'pour_jug1_to_jug2': pour_jug1_to_jug2,
    'pour_jug2_to_jug1': pour_jug2_to_jug1
}

# Example usage
initial_state = (0, 0)
goal_state = (2, 0)

path = bfs(initial_state, goal_state)
if path:
    print("Solution found:")
    for i, action in enumerate(path, 1):
        print(f"Step {i}: {action}")
else:
    print("No solution found.")
