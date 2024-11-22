from geopy.distance import geodesic

# Uses geopy to filter for locations in a certain range
def filter_places_by_radius(center, data, desired_radius, tolerance=100):
    """Filter places based on distance from a central point."""
    results_within_radius = []

    for place in data["results"]:
        place_coord = (place["geometry"]["location"]["lat"], place["geometry"]["location"]["lng"])
        distance = geodesic(center, place_coord).meters

        if distance <= desired_radius + tolerance:
                # Ensure 'rating' key exists before accessing it
            rating = place.get('rating', None)
            if rating is not None:
                results_within_radius.append((place['name'], place['vicinity'], distance, rating))

    # print(results_within_radius)

    # Sort the results by rating in descending order and pick the top 3
    top_three_places = sorted(results_within_radius, key=lambda x: x[3], reverse=True)[:3]

    # print(top_three_places)

    return top_three_places
