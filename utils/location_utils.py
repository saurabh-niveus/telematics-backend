import random
from data.indian_data import INDIAN_CITIES

def get_random_indian_location():
    city_data = random.choice(INDIAN_CITIES)
    # Add some random variation to the exact coordinates
    lat_variation = random.uniform(-0.1, 0.1)
    lng_variation = random.uniform(-0.1, 0.1)
    
    return {
        "lat": city_data["lat"] + lat_variation,
        "lng": city_data["lng"] + lng_variation,
        "country": "India",
        "state": city_data["state"],
        "city": city_data["city"]
    }
