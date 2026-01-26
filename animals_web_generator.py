import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ""
for animal_data in animals_data:
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_data["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += f'<strong>Diet:</strong> {animal_data["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> {animal_data["locations"][0]}<br/>\n'
    try:
        output += f'<strong>Type:</strong> {animal_data["characteristics"]["type"]}<br/>\n'
    except:
        output += '</p>'
        output += '</li>'
        continue
    output += '</p>'
    output += '</li>'

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_inhalt = file.read()

animals_html = html_inhalt.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(animals_html)

