import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
  """ Loads a JSON data from api """
  url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  headers = {'X-Api-Key': API_KEY}
  response = requests.get(url, headers=headers)
  data = response.json()
  return data
