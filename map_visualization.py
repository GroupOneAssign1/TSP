from geopy.distance import geodesic

# Compute distances between each pair of consecutive cities in the route
city_distances = []
for i in range(len(route_geo) - 1):
    city1 = route_geo[i]
    city2 = route_geo[i + 1]
    coord1 = city_coords_geo[city1]
    coord2 = city_coords_geo[city2]
    distance_km = geodesic(coord1, coord2).kilometers
    city_distances.append((city1, city2, distance_km))

# Recreate the plot with distances shown
plt.figure(figsize=(10, 6))
plt.plot(longitudes, latitudes, marker='o', linestyle='-', color='darkorange')

# Annotate cities
for city in route_geo:
    lat, lon = city_coords_geo[city]
    plt.text(lon + 0.05, lat + 0.02, city, fontsize=12)

# Annotate distances between cities
for i, (city1, city2, dist) in enumerate(city_distances):
    lat1, lon1 = city_coords_geo[city1]
    lat2, lon2 = city_coords_geo[city2]
    mid_lat = (lat1 + lat2) / 2
    mid_lon = (lon1 + lon2) / 2
    plt.text(mid_lon, mid_lat, f"{dist:.1f} km", fontsize=10, color='blue')

# Final touches
plt.title("TSP Route in Kenya")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.tight_layout()

# Save updated plot with distances
geo_distance_plot_path = "/mnt/data/tsp_route_kenya_geo_distances.png"
plt.savefig(geo_distance_plot_path)
geo_distance_plot_path
