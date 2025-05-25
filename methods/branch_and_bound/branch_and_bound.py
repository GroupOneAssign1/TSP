# Branch and Bound Code
import math

def calculate_path_distance(path, distances):
    """Calculate the total distance of a path."""
    total_distance = 0
    for i in range(len(path) - 1):
        from_city = path[i]
        to_city = path[i + 1]
        if from_city in distances and to_city in distances[from_city]:
            total_distance += distances[from_city][to_city]
        else:
            return float('inf')
    return total_distance

def branch_and_bound_tsp(distances, start_city):
    """
    Solve TSP using branch and bound approach.

    Args:
        distances (dict): Nested dict distances[from_city][to_city] = dist.
        start_city (str): Starting city for the route.

    Returns:
        (list, float): The shortest path and its distance.
    """

    cities = list(distances.keys())
    n = len(cities)
    best_cost = float('inf')  # Keep track of best cost found so far (initially infinity)
    best_path = None

    def bound(path, current_cost):
        """
        Lower bound estimate for completing the tour starting with 'path'.

        The bound estimates the minimum possible cost to complete the route
        by adding:
          - the cost already incurred on the path (current_cost),
          - the minimum cost to go from the last city in path to any unvisited city (min_out),
          - plus an optimistic estimate for visiting all remaining unvisited cities (min_incoming).

        This bound helps prune the search tree if this minimum estimated cost
        already exceeds the best known cost, meaning this path can't improve.

        Args:
            path (list): Current partial path of visited cities.
            current_cost (float): Cost accumulated so far.

        Returns:
            float: Lower bound on total tour cost if we continue from this path.
        """

        # 1. Identify unvisited cities
        unvisited = [c for c in cities if c not in path]

        # 2. Minimum cost from the last visited city to any unvisited city
        last_city = path[-1]
        min_out = float('inf')
        for city in unvisited:
            if last_city in distances and city in distances[last_city]:
                # Check the smallest "exit edge" cost from last_city to next unvisited city
                if distances[last_city][city] < min_out:
                    min_out = distances[last_city][city]

        # If no unvisited cities remain, min_out is cost to return to start city
        if not unvisited:
            if last_city in distances and start_city in distances[last_city]:
                min_out = distances[last_city][start_city]
            else:
                min_out = float('inf')

        # 3. Optimistic estimate of the cost to cover all unvisited cities:
        # For each unvisited city, find the minimum edge cost leading out from that city.
        # Summing these gives a heuristic minimum cost to "connect" the remaining cities.
        min_incoming = 0
        for city in unvisited:
            min_edge = float('inf')
            for other in cities:
                if other != city and city in distances and other in distances[city]:
                    if distances[city][other] < min_edge:
                        min_edge = distances[city][other]
            # If min_edge is inf (no edges), just skip (could make path invalid)
            if min_edge != float('inf'):
                min_incoming += min_edge

        # 4. Return the sum as the lower bound:
        # current_cost + cost to leave last city + minimum edges to cover unvisited
        return current_cost + min_out + min_incoming

    def backtrack(path, current_cost):
        nonlocal best_cost, best_path

        # If all cities visited, close the tour by returning to start
        if len(path) == n:
            last_city = path[-1]
            if start_city in distances[last_city]:
                total_cost = current_cost + distances[last_city][start_city]
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = path + [start_city]
            return

        # Prune the branch if lower bound is already worse than best known cost
        if bound(path, current_cost) >= best_cost:
            # No need to explore further since we cannot do better
            return

        # Try to extend path by visiting unvisited cities
        for city in cities:
            if city not in path:
                last_city = path[-1]
                # Only consider edges that exist to avoid invalid paths
                if last_city in distances and city in distances[last_city]:
                    new_cost = current_cost + distances[last_city][city]
                    # Further pruning: if new_cost already exceeds best_cost, skip
                    if new_cost < best_cost:
                        backtrack(path + [city], new_cost)

    # Start recursion from start city with cost 0
    backtrack([start_city], 0)

    return best_path, best_cost

if __name__ == "__main__":
    city_names = ["Nairobi", "Nandi", "Meru", "Nakuru", "Nyeri", "Kericho"]

    distances_data = {
        "Nandi": {"Kericho": 95, "Nakuru": 156, "Nairobi": 313, "Meru": 409, "Nyeri": 320},
        "Nakuru": {"Nandi": 156, "Kericho": 107, "Meru": 256, "Nyeri": 167, "Nairobi": 163},
        "Meru": {"Nandi": 409, "Kericho": 360, "Nakuru": 256, "Nyeri": 137, "Nairobi": 226},
        "Nyeri": {"Nandi": 320, "Kericho": 271, "Nakuru": 167, "Meru": 137, "Nairobi": 151},
        "Kericho": {"Nandi": 95, "Nakuru": 107, "Meru": 360, "Nyeri": 271, "Nairobi": 264},
        "Nairobi": {"Nandi": 313, "Kericho": 264, "Nakuru": 163, "Nyeri": 151, "Meru": 226}
    }

    start_city = "Nairobi"

    shortest_route, total_dist = branch_and_bound_tsp(distances_data, start_city)

    if shortest_route and total_dist != float('inf'):
        print(f"Branch and Bound Shortest Route: {' -> '.join(shortest_route)}")
        print(f"Total Distance: {total_dist} km")
    else:
        print("No valid route found.")
