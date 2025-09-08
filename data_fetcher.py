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

    Raises:
        ValueError: If API_KEY is not set or response is invalid.
        requests.RequestException: If network/API request fails.
    """
    if not API_KEY:
        raise ValueError("API_NINJAS_KEY environment variable not set.")

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()

    try:
        data = response.json()
    except ValueError:
        raise ValueError("Failed to decode JSON response from API.")

    if not isinstance(data, list):
        raise ValueError(
            f"Unexpected API response format. Expected list, got {type(data)}."
        )

    return data
