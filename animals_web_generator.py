import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ""
for animal_data in animals_data:
    output += '<li class="cards_item">'
    output += f'Name: {animal_data["name"]}<br/>\n'
    output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
    output += f"Location: {animal_data['locations'][0]}<br/>\n"
    try:
        output += f"Type: {animal_data['characteristics']['type']}<br/>\n"
    except:
        output += "<br/>\n"
        output += '</li>'
        continue
    output += "<br/>\n"
    output += '</li>'

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_inhalt = file.read()

animals_html = html_inhalt.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(animals_html)

