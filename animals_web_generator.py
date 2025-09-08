import html
import requests
import data_fetcher


def serialize_animal(animal_obj: dict) -> str:
    """Convert a single animal object into an HTML card."""
    name = html.escape(animal_obj.get("name", "Unknown"))
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    diet = html.escape(characteristics.get("diet", "Unknown"))
    animal_type = html.escape(characteristics.get("type", "Unknown"))
    skin_type = html.escape(characteristics.get("skin_type", "Unknown"))
    locations_str = ", ".join(html.escape(loc) for loc in locations)

    return (
        f'<li class="cards__item">\n'
        f'  <div class="card__title">{name}</div>\n'
        f'  <div class="card__text">\n'
        f'    <ul class="card__fields">\n'
        f'      <li><strong>Diet:</strong> {diet}</li>\n'
        f'      <li><strong>Location:</strong> {locations_str or "Unknown"}</li>\n'
        f'      <li><strong>Type:</strong> {animal_type}</li>\n'
        f'      <li><strong>Skin Type:</strong> {skin_type}</li>\n'
        f'    </ul>\n'
        f'  </div>\n'
        f'</li>\n'
    )


def generate_animals_html(data: list[dict]) -> str:
    """Generate HTML for all animals."""
    sorted_data = sorted(data, key=lambda x: x.get("name") or "")
    return "".join(serialize_animal(animal) for animal in sorted_data)


def create_html_page(animals_html: str, query: str) -> str:
    """Return full HTML page string with styling."""
    query_safe = html.escape(query)
    content = (
        animals_html
        if animals_html
        else f"<h2>The animal '{query_safe}' doesn't exist.</h2>"
    )
    return f"""<html>
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
    {content}
  </ul>
</body>
</html>
"""


def main():
    """Main program flow."""
    animal_name = input("Please enter an animal: ").strip()

    try:
        data = data_fetcher.fetch_data(animal_name)
        animals_html = generate_animals_html(data) if data else ""
        full_html = create_html_page(animals_html, animal_name)

        with open("animals.html", "w", encoding="utf-8") as f:
            f.write(full_html)

        if data:
            print(f"✅ Website generated with {len(data)} animal(s).")
        else:
            print(
                f"ℹ️ No results found. Error page created in animals.html."
            )

    except requests.RequestException as req_err:
        print(f"❌ Network/API error: {req_err}")
    except ValueError as val_err:
        print(f"❌ Data error: {val_err}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
