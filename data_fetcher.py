import os
import requests
from dotenv import load_dotenv

# Load .env from the same folder as this file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_NINJAS_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"



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
print(API_KEY)