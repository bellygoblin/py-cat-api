import os
from the_cat_api.rest_adapter import RestAdapter
from the_cat_api.models import Result, Weight, Breed
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def main():
  catapi = RestAdapter(api_key=os.getenv("API_KEY"))
  result = catapi.get("breeds")
  breed_list = []
  for d in result.data:
    breed_list.append(Breed(**d))
  print(breed_list[0].weight)

main()