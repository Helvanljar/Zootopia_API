import json
import os


def load_data(file_path):
    """Load JSON file containing animal data with error handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON: {e}")


def serialize_animal(animal_obj):
    """Serialize a single animal object into HTML using nested <ul>."""
    output = '<li class="cards__item">\n'

    # Name
    name = animal_obj.get("name", "Unknown")
    output += f"  <div class='card__title'>{name}</div>\n"

    output += "  <div class='card__text'>\n    <ul class='card__fields'>\n"

    # Characteristics (safe lookup)
    characteristics = animal_obj.get("characteristics", {})

    # Diet
    if "diet" in characteristics:
        output += f"      <li><strong>Diet:</strong> {characteristics['diet']}</li>\n"

    # Locations
    locations = animal_obj.get("locations", [])
    if locations:
        locations_str = ", ".join(locations)
        output += f"      <li><strong>Location:</strong> {locations_str}</li>\n"

    # Type
    if "type" in characteristics:
        output += f"      <li><strong>Type:</strong> {characteristics['type']}</li>\n"

    # Skin Type (with fallback)
    output += f"      <li><strong>Skin Type:</strong> {characteristics.get('skin_type', 'Unknown')}</li>\n"

    output += "    </ul>\n  </div>\n</li>\n"
    return output


def generate_animals_html(data):
    """Generate HTML for all animals by serializing each one."""
    # Sort alphabetically by name with safe fallback
    sorted_data = sorted(data, key=lambda x: x.get("name") or "")
    return "".join(serialize_animal(animal) for animal in sorted_data)


def create_html_page(animals_html):
    """Return the full HTML page as a string."""
    return f"""
<html>
<head>
  <meta charset="UTF-8">
  <title>My Animal Repository</title>
  <style>
    html {{ background-color: #ffe9e9; }}
    body {{
      font-family: 'Roboto','Helvetica Neue', Helvetica, Arial, sans-serif;
      padding: 1rem;
      width: 900px;
      margin: auto;
    }}
    h1 {{
      text-align: center;
      font-size: 40pt;
      font-weight: normal;
    }}
    .cards {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .cards__item {{
      background-color: white;
      border-radius: 0.25rem;
      box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
      overflow: hidden;
      padding: 1rem;
      margin: 50px 0;
    }}
    .card__title {{
      font-size: 1.25rem;
      font-weight: 300;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }}
    .card__text {{
      font-size: 0.95rem;
      line-height: 1.5;
    }}
    .card__fields {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .card__fields li {{
      padding: 2px 0;
    }}
  </style>
</head>
<body>
  <h1>My Animal Repository</h1>
  <ul class="cards">
    {animals_html}
  </ul>
</body>
</html>
"""


def main():
    try:
        data = load_data("animals_data.json")
        animals_html = generate_animals_html(data)
        full_html = create_html_page(animals_html)

        with open("animals.html", "w") as f:
            f.write(full_html)

        print(f"✅ HTML file generated with {len(data)} animals.")
    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
