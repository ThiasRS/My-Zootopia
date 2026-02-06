from source import data_fetcher, animals_web_generator


def main():
    """Takes the data and creates the animals.html"""
    animal_name = animals_web_generator.user_picks_animal()

    animals_data = data_fetcher.fetch_data(animal_name)


    output = ""
    if not animals_data:
        output = f'<h2 style="text-align: center;">The animal {animal_name} does not exist.</h2>'
    else:
        for animal_data in animals_data:
            output += animals_web_generator.serialize_animal(animal_data)

    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_inhalt = file.read()

    animals_html = html_inhalt.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(animals_html)

    print("Website was successfully generated to the file animals.html")


if __name__ == "__main__":
    main()