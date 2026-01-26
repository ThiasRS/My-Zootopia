import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ""
for animal_data in animals_data:
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"
    output += f"Location: {animal_data['locations'][0]}\n"
    try:
        output += f"Type: {animal_data['characteristics']['type']}\n"
    except:
        output += "\n"
        continue
    output += "\n"




