import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def serialize_animal(animal_obj):
    name = animal_obj.get("name", "Unknown Animal")
    diet = animal_obj["characteristics"].get("diet", "Unknown")
    location = animal_obj["locations"][0] if animal_obj.get("locations") else "Unknown"
    animal_type = animal_obj["characteristics"].get("type")

    output = f'<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += f'  <br/>\n'
    output += f'  <div class="card__text">\n'
    output += f'    <ul>\n'
    output += f'      <li><strong>Diet:</strong> {diet}</li>\n'
    output += f'      <li><strong>Location:</strong> {location}</li>\n'

    if animal_type:
        output += f'      <li><strong>Type:</strong> {animal_type}</li>\n'

    output += f'    </ul>\n'
    output += f'  </div>\n'
    output += f'</li>'

    return output


animals_data = load_data('animals_data.json')

output = ""
for animal_data in animals_data:
    output += serialize_animal(animal_data)

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_inhalt = file.read()

animals_html = html_inhalt.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(animals_html)

