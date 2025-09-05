import os
import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_NINJAS_KEY")  # Set your API key in environment


def fetch_data(animal_name: str) -> list[dict]:
    """
    Fetches the animals data for the given 'animal_name'.

    Returns:
        A list of animals, each animal is a dictionary:
        {
            'name': ...,
            'taxonomy': { ... },
            'locations': [ ... ],
            'characteristics': { ... }
        }
    """
    if not API_KEY:
        raise ValueError("API_NINJAS_KEY environment variable not set.")

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()

    return response.json()
