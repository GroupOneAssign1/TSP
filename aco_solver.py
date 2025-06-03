import random
import numpy as np

class AntColony:
    def __init__(self, distance_matrix, n_ants, n_iterations, decay, alpha=1, beta=2):
        self.distance_matrix = np.array(distance_matrix)
        self.pheromone = np.ones(self.distance_matrix.shape) / len(distance_matrix)
        self.all_inds = range(len(distance_matrix))
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        all_time_shortest_path = ([], float('inf'))
        for _ in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheromone(all_paths)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            self.pheromone *= (1 - self.decay)
        return all_time_shortest_path

    def gen_path_dist(self, path):
        total_dist = 0
        for i in range(len(path) - 1):
            total_dist += self.distance_matrix[path[i]][path[i + 1]]
        total_dist += self.distance_matrix[path[-1]][path[0]]  # return to start
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.gen_path(0)  # Start from node 0
            dist = self.gen_path_dist(path)
            all_paths.append((path, dist))
        return all_paths

    def gen_path(self, start):
        path = [start]
        visited = set(path)
        for _ in range(len(self.distance_matrix) - 1):
            move = self.pick_move(path[-1], visited)
            path.append(move)
            visited.add(move)
        return path

    def pick_move(self, current, visited):
        pheromone = np.copy(self.pheromone[current])
        pheromone[list(visited)] = 0

        distances = np.copy(self.distance_matrix[current])
        distances[list(visited)] = np.inf  # prevent 1/0 and revisiting

        with np.errstate(divide='ignore'):  # ignore divide by zero warning
            attractiveness = pheromone ** self.alpha * ((1.0 / distances) ** self.beta)

        attractiveness[np.isinf(attractiveness)] = 0  # clean up infinities

        total = attractiveness.sum()
        if total == 0:
            probabilities = np.ones(len(attractiveness))
            probabilities[list(visited)] = 0
            probabilities /= probabilities.sum()
        else:
            probabilities = attractiveness / total

        return np.random.choice(self.all_inds, p=probabilities)

    def spread_pheromone(self, all_paths):
        for path, dist in all_paths:
            for i in range(len(path)):
                from_city = path[i]
                to_city = path[(i + 1) % len(path)]
                self.pheromone[from_city][to_city] += 1.0 / dist
                self.pheromone[to_city][from_city] += 1.0 / dist


if __name__ == '__main__':
    county_names = ["Nandi", "Kericho", "Nakuru", "Nairobi", "Meru", "Nyeri"]

    distances_data = {
        "Nandi": {"Kericho": 95, "Nakuru": 156, "Nairobi": 313, "Meru": 409, "Nyeri": 320},
        "Kericho": {"Nandi": 95, "Nakuru": 107, "Meru": 360, "Nyeri": 271, "Nairobi": 264},
        "Nakuru": {"Nandi": 156, "Kericho": 107, "Meru": 256, "Nyeri": 167, "Nairobi": 163},
        "Nairobi": {"Nandi": 313, "Kericho": 264, "Nakuru": 163, "Nyeri": 151, "Meru": 226},
        "Meru": {"Nandi": 409, "Kericho": 360, "Nakuru": 256, "Nyeri": 137, "Nairobi": 226},
        "Nyeri": {"Nandi": 320, "Kericho": 271, "Nakuru": 167, "Meru": 137, "Nairobi": 151}
    }

    # Convert dict to 2D matrix, use np.inf for missing paths and diagonal
    n = len(county_names)
    distance_matrix = []
    for from_city in county_names:
        row = []
        for to_city in county_names:
            if from_city == to_city:
                row.append(np.inf)  # prevent zero distance to self
            else:
                row.append(distances_data[from_city][to_city])
        distance_matrix.append(row)

    colony = AntColony(distance_matrix, n_ants=10, n_iterations=100, decay=0.1, alpha=1, beta=2)
    shortest_path, cost = colony.run()
    named_path = [county_names[i] for i in shortest_path]

    print("\nBest Route (ACO):")
    print(" ➜ ".join(named_path))
    print(f"Total Distance: {round(cost, 2)} km")
