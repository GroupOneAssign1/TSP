
import openrouteservice
from openrouteservice import Client
import pandas as pd
import itertools

API_KEY = '5b3ce3597851110001cf62482d6195c9c66a4ae9bdeffab47d3d9cc9'

client = openrouteservice.Client(key=API_KEY)

locations = {

    'Nairobi': (36.8219, -1.2921),
    'Nyeri': (36.9500, -0.4167),
    'Meru': (37.6497, 0.0470),
    'Nakuru': (36.0800, -0.3031),
    'Kericho': (35.2831, -0.3670),
    'Nandi': (35.1500, 0.1833)
}

#convert to co-ordinates lists and names
coords = list(locations.values())
county_names = list(locations.keys())

#request distances matrix from openrouteservice
response = client.distance_matrix(
    locations=coords,
    profile='driving-car',
    metrics=['distance'],
    resolve_locations=False

)

#convert distances to kilometers
distances_km = [[round(d / 1000, 2) for d in row]for row in response['distances']]

#save matrix for reference
df = pd.DataFrame(distances_km, index=county_names, columns=county_names)
df.to_csv("distance_matrix.csv")
print("Distance matrix saved to 'distance_matrix.csv'.")

# brute force TSP algorithm
def tsp_brute_force(distance_matrix, start_index=0):
    n =len(distance_matrix)
    cities = list(range(n))
    cities.remove(start_index)
    min_cost = float('inf')
    best_path =[]

    for perm in itertools.permutations(cities):
        current_cost = 0
        k =start_index
        path =[start_index]
        for j in perm:
            current_cost += distance_matrix[k][j]
            k=j
            path.append(j)
        current_cost += distance_matrix[k][start_index] # return to start
        path.append(start_index)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = path

    return best_path, round(min_cost, 2)

# Run TSP
path, cost = tsp_brute_force(distances_km, start_index=0)

# map path indexes to county names
named_path = [county_names[i] for i in path]

print("\n Best Route (Brute Force):")
print("➜".join(named_path))
print(f" Total Distance: {cost} km")

