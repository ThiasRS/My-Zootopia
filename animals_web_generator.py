import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal_data in animals_data:
    print(f"Name: {animal_data['name']}")
    print(f"Diet: {animal_data['characteristics']['diet']}")
    print(f"Location: {animal_data['locations'][0]}")
    try:
        print(f"Type: {animal_data['characteristics']['type']}")
    except:
        print("")
        continue
    print("")

