from typing import List, Dict, Union

class Result:
  def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
    """
    Result returned from low-level RestAdapter
    :param status_code: Standard HTTP Status code
    :param message: Human readable result
    :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
    """
    self.status_code = int(status_code)
    self.message = str(message)
    self.data = data if data else []

class Fact:
  def __init__(self, id: str, text: str, language_code: str, breed_id: str):
    self.id = id
    self.text = text
    self.language_code = language_code
    self.breed_id = breed_id

class Image:
    id: str
    width: int
    height: int
    url: str

    def __init__(self, id: str, width: int, height: int, url: str) -> None:
        self.id = id
        self.width = width
        self.height = height
        self.url = url


class Weight:
    imperial: str
    metric: str

    def __init__(self, imperial: str, metric: str) -> None:
        self.imperial = imperial
        self.metric = metric


class Breed:
    weight: Weight
    id: str
    name: str
    cfa_url: str
    vetstreet_url: str
    vcahospitals_url: str
    temperament: str
    origin: str
    country_codes: str
    country_code: str
    description: str
    life_span: str
    indoor: int
    lap: int
    alt_names: str
    adaptability: int
    affection_level: int
    child_friendly: int
    dog_friendly: int
    energy_level: int
    grooming: int
    health_issues: int
    intelligence: int
    shedding_level: int
    social_needs: int
    stranger_friendly: int
    vocalisation: int
    experimental: int
    hairless: int
    natural: int
    rare: int
    rex: int
    suppressed_tail: int
    short_legs: int
    wikipedia_url: str
    hypoallergenic: int
    reference_image_id: str
    image: Image

    def __init__(self, weight: Weight, id: str, name: str, country_codes: str, country_code: str, description: str, 
                 temperament: str = '', origin: str = '', life_span: str = '', alt_names: str = '', 
                 wikipedia_url: str = '', **kwargs) -> None:
        self.weight = Weight(**weight) if isinstance(weight, dict) else weight
        self.id = id
        self.name = name
        self.origin = origin
        self.country_codes = country_codes
        self.country_code = country_code
        self.description = description
        self.temperament = temperament
        self.life_span = life_span
        self.alt_names = alt_names
        self.wikipedia_url = wikipedia_url
        self.__dict__.update(kwargs)
