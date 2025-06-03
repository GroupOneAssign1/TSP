import random
import math

# ---- Problem Setup ----

# Sample distance matrix (symmetric)
distances = [
    [0, 2, 2, 5],
    [2, 0, 3, 4],
    [2, 3, 0, 1],
    [5, 4, 1, 0]
]

num_cities = len(distances)
num_ants = 10
num_iterations = 100
alpha = 1        # pheromone importance
beta = 2         # distance importance
evaporation = 0.5
Q = 100          # total pheromone deposited

# ---- Initialization ----

pheromone = [[1 for _ in range(num_cities)] for _ in range(num_cities)]

def distance(city1, city2):
    return distances[city1][city2]

def initialize_ants():
    return [random.randint(0, num_cities - 1) for _ in range(num_ants)]

def probability(city_i, city_j, visited):
    pher = pheromone[city_i][city_j] ** alpha
    dist = (1 / distances[city_i][city_j]) ** beta
    return pher * dist if city_j not in visited else 0

# ---- Core ACO Logic ----

def construct_solution(start_city):
    path = [start_city]
    total_distance = 0

    while len(path) < num_cities:
        current = path[-1]
        probs = [probability(current, j, path) for j in range(num_cities)]
        total = sum(probs)
        if total == 0:
            return path, float('inf')  # dead end
        probs = [p / total for p in probs]
        next_city = random.choices(range(num_cities), weights=probs)[0]
        path.append(next_city)
        total_distance += distance(current, next_city)

    total_distance += distance(path[-1], path[0])  # Return to start
    return path, total_distance

def update_pheromones(solutions):
    # Evaporate
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1 - evaporation)

    # Deposit
    for path, dist in solutions:
        deposit = Q / dist
        for i in range(len(path)):
            from_city = path[i]
            to_city = path[(i + 1) % num_cities]
            pheromone[from_city][to_city] += deposit
            pheromone[to_city][from_city] += deposit  # symmetric

# ---- Main Loop ----

best_path = None
best_distance = float('inf')

for iteration in range(num_iterations):
    ants = initialize_ants()
    solutions = []

    for ant in ants:
        path, dist = construct_solution(ant)
        solutions.append((path, dist))
        if dist < best_distance:
            best_path = path
            best_distance = dist

    update_pheromones(solutions)
    print(f"Iteration {iteration + 1}: Best distance so far = {best_distance}")

print("\nBest path found:", best_path)
print("Distance:", best_distance)
