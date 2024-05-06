import random

# Distance matrix representing distances between cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def total_distance(path):
    total = 0
    for i in range(len(path) - 1):
        total += distance_matrix[path[i]][path[i+1]]
    total += distance_matrix[path[-1]][path[0]]  # Return to starting city
    return total

def hill_climbing_tsp(num_cities):
    current_path = list(range(num_cities))
    current_distance = total_distance(current_path) 
    for _ in range(10000):
        neighbor_path = current_path[:]
        i, j = random.sample(range(num_cities), 2)
        neighbor_path[i], neighbor_path[j] = neighbor_path[j], neighbor_path[i]
        neighbor_distance = total_distance(neighbor_path)
        if neighbor_distance < current_distance:
            current_path = neighbor_path
            current_distance = neighbor_distance
    return current_path

def main():
    num_cities = 4
    solution = hill_climbing_tsp(num_cities)
    print("Optimal path:", solution)
    print("Total distance:", total_distance(solution))

if __name__ == "__main__":
    main()
