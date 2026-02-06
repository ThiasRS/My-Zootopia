import requests

API_KEY = 'pPjwC3Sg9pkXPuSlj562gqEAILOtkOZJ6OT2wqAu'


def fetch_data(animal_name):
  """ Loads a JSON data from api """
  url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  headers = {'X-Api-Key': API_KEY}
  response = requests.get(url, headers=headers)
  data = response.json()
  return data