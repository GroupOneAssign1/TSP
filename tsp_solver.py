import itertools
import math

def calculate_path_distance(path, distances):
    """
    Calculates the total distance of a given path.

    Args:
        path (list): A list of city names representing the order of visitation.
                     The path includes the starting city, intermediate cities,
                     and the return to the starting city.
        distances (dict): A dictionary representing the distance matrix.
                          distances[city_a][city_b] gives the distance
                          between city_a and city_b.

    Returns:
        float: The total distance of the path. Returns float('inf') if any
               segment of the path does not have a defined distance.
    """
    total_distance = 0
    for i in range(len(path) - 1):
        from_city = path[i]
        to_city = path[i+1]
        if from_city in distances and to_city in distances[from_city]:
            total_distance += distances[from_city][to_city]
        else:
            # Handle cases where a path segment might not exist, making the path invalid
            return float('inf')
    return total_distance

def find_shortest_route(locations, distances, start_location):
    """
    Finds the shortest possible route that visits all given locations
    exactly once and returns to the start_location.

    Args:
        locations (list): A list of all location names (strings).
        distances (dict): A dictionary representing the distance matrix.
                          distances[city_a][city_b] gives the distance
                          between city_a and city_b.
        start_location (str): The name of the starting and ending location.

    Returns:
        tuple: A tuple containing:
               - list: The shortest path (list of location names).
               - float: The total distance of the shortest path.
               Returns (None, float('inf')) if no valid path is found.
    """
    if start_location not in locations:
        print(f"Error: Start location '{start_location}' not in the list of locations.")
        return None, float('inf')

    # Create a list of cities to visit, excluding the start_location
    cities_to_visit = [city for city in locations if city != start_location]

    min_distance = float('inf')
    shortest_path_names = []

    # Generate all permutations of visiting the other cities
    for permutation_of_cities in itertools.permutations(cities_to_visit):
        # Construct the full path: start -> permutation -> start
        current_path_names = [start_location] + list(permutation_of_cities) + [start_location]

        # Calculate distance for the current path
        dist = calculate_path_distance(current_path_names, distances)

        # Update shortest path if current path is shorter and valid
        if dist < min_distance:
            min_distance = dist
            shortest_path_names = current_path_names

    if shortest_path_names:
        return shortest_path_names, min_distance
    else:
        return None, float('inf')

if __name__ == "__main__":
    # --- Data directly provided by you ---

    # 1. Define your locations (all the unique cities)
    city_names = ["Nairobi", "Nandi", "Meru", "Nakuru", "Nyeri", "Kericho"]

    # 2. Define the distances between locations (adjacency matrix as a dictionary)
    #    distances[from_city][to_city] = distance
    #    All connections are assumed to be symmetric (distance is the same both ways).
    distances_data = {
        "Nandi": {
            "Kericho": 95,
            "Nakuru": 156,
            "Nairobi": 313,
            "Meru": 409,
            "Nyeri": 320
        },
        "Nakuru": {
            "Nandi": 156,
            "Kericho": 107,
            "Meru": 256,
            "Nyeri": 167,
            "Nairobi": 163
        },
        "Meru": {
            "Nandi": 409,
            "Kericho": 360,
            "Nakuru": 256,
            "Nyeri": 137,
            "Nairobi": 226
        },
        "Nyeri": {
            "Nandi": 320,
            "Kericho": 271,
            "Nakuru": 167,
            "Meru": 137,
            "Nairobi": 151
        },
        "Kericho": {
            "Nandi": 95,
            "Nakuru": 107,
            "Meru": 360,
            "Nyeri": 271,
            "Nairobi": 264
        },
        "Nairobi": {
            "Nandi": 313,
            "Kericho": 264,
            "Nakuru": 163,
            "Nyeri": 151,
            "Meru": 226
        }
    }

    # 3. Define the starting point
    start_city = "Nairobi"

    print(f"Finding shortest route starting from '{start_city}' for cities: {city_names}")
    print("--- Confirmed Distances ---")
    # A cleaner way to print all unique connections and their distances for confirmation
    all_connections_printed = set() # Use a set to avoid printing symmetric connections twice
    for city1, connections in distances_data.items():
        for city2, dist in connections.items():
            # Add a canonical representation of the connection to the set
            # e.g., frozenset({'CityA', 'CityB'}) ensures order doesn't matter for uniqueness
            connection_pair = frozenset({city1, city2})
            if connection_pair not in all_connections_printed:
                print(f"  {city1} <-> {city2}: {dist} km")
                all_connections_printed.add(connection_pair)
    print("-" * 30)

    # Run the TSP solver
    shortest_route, total_dist = find_shortest_route(city_names, distances_data, start_city)

    if shortest_route and total_dist != float('inf'):
        print(f"Shortest Route: {' -> '.join(shortest_route)}")
        print(f"Total Distance: {total_dist} km")
    else:
        print("Could not find a valid route. This might happen if the graph is not fully connected, preventing a complete tour.")
        
