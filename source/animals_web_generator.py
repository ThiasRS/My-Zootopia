import data_fetcher


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


def user_picks_animal():
    """User input to choose animal name"""
    while True:
        animal_name = str(input('Type in an animal name to create a website: '))
        if animal_name == "":
            print('Empty input, type in an animal name!')
        else:
            break
    return animal_name


