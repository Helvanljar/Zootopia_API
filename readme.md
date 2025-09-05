# Zootopia API Project

## Project Description
The Zootopia API Project is a Python program that fetches animal data from the [API Ninjas Animals API](https://api.api-ninjas.com/) and generates an HTML website displaying information about animals. Users can type the name of an animal, and the program will show details such as diet, location, type, and skin type for that animal and related species.

This project allows users to explore animal information dynamically without manually collecting or formatting data. It is intended for beginners and students learning Python, APIs, and basic HTML generation.

## Installation, Setup & Usage

1. Clone the repository and enter the project folder:
```
git clone https://github.com/Helvanljar/Zootopia_API.git
cd Zootopia_API
```

2. (Optional) Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```
Dependencies included are `requests` and `python-dotenv`.

4. Set up your API key:
Create a `.env` file in the project root and add your API key from API Ninjas:
```
API_NINJAS_KEY=your_actual_api_key_here
```
Make sure `.env` is included in `.gitignore` to avoid committing it, along with `__pycache__/`, `*.pyc`, and `animals.html`.

5. Run the program:
```
python3 animals_web_generator.py
```
Follow the prompt to enter an animal name (e.g., `Fox` or `Owl`). The program will generate `animals.html` in the same folder. Open this file in a browser to see the results.

**Examples:**
- Existing animal:
```
Please enter an animal: Fox
Website generated with 12 animal(s).
```
- Non-existent animal:
```
Please enter an animal: UnknownAnimal
No results found. A friendly message was generated in animals.html.
```

## Project Structure
```
Zootopia_API/
├─ animals_web_generator.py    # Generates the HTML website
├─ data_fetcher.py             # Handles API requests
├─ requirements.txt            # Lists project dependencies
├─ .env                        # Stores API key (ignored by Git)
├─ .gitignore                  # Ignores sensitive/local files
├─ README.md                   # This documentation
└─ animals.html                # Generated HTML output
```

## Git Notes
- Pull remote changes before pushing:
```
git pull origin main
git push origin main
```
- Force push only if necessary:
```
git push -f origin main
```
- If `.env` was accidentally tracked:
```
git rm --cached .env
git commit -m "Stop tracking .env"
```

## Contributing
We welcome contributions! Fork the repository, create a branch for your feature or bug fix, make your changes and test locally, then submit a pull request with a clear description.

## License
This project is open-source and free to use.

