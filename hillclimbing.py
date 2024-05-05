import random

def objective_function(x):
    """
    Objective function to maximize. 
    This is just an example function, you can replace it with any other function.
    """
    return -(x ** 2)

def random_neighbor(solution, step_size):
    """
    Generate a random neighbor of the current solution.
    """
    return solution + random.uniform(-step_size, step_size)

def hill_climbing(objective_function, initial_solution, step_size, max_iter):
    """
    Hill Climbing Algorithm to maximize the objective function.
    """
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    for _ in range(max_iter):
        neighbor = random_neighbor(current_solution, step_size)
        neighbor_value = objective_function(neighbor)

        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value

    return current_solution, current_value

# Define the initial solution and algorithm parameters
initial_solution = random.uniform(-10, 10)
step_size = 0.1
max_iter = 1000

# Run the algorithm
best_solution, best_value = hill_climbing(objective_function, initial_solution, step_size, max_iter)

print("Best solution:", best_solution)
print("Best value:", best_value)
