import random
from character import Character
from dynasty import Dynasty

DYNASTY_NAMES = ['RoughRiders', 'HungrySquirrels',
                 'CowardlyPythons', 'LuckyFrogs', 'TerrifyingBubbles']


def create_dynasty(dynasties: set = {}, id: int = 1, culture: str = 'english'):
    name = random.choice(DYNASTY_NAMES)
    while Dynasty.find(dynasties=dynasties, name=name):
        name = random.choice(DYNASTY_NAMES)

    dynasty = Dynasty(id=id, name=name, culture=culture)
    return dynasty


def create_character(names: list = [], characters: set = {}, dynasty: Dynasty = None, religion: str = "catholic", culture: str = "english", id: int = 3, father_id: int = 1, mother_id: int = 2, birth_date: str = "0001.01.01", death_date: str = "0081.01.01"):
    name = random.choice(names)
    character = Character(id=id, dynasty=dynasty, name=name, religion=religion,
                          culture=culture, father_id=father_id, mother_id=mother_id, birth_date=birth_date, death_date=death_date)
    if Character.find(characters=characters, name=name):
        shared_name_character = Character.find(
            characters=characters, name=name)
        while shared_name_character.is_sibling(character):
            character = create_character(
                names, characters, dynasty, religion, culture, id, father_id, mother_id, birth_date, death_date)
    return character


def initialize(names: list = [], initial_id: int = 1):
    dynasties = set()
    characters = set()
    initial_religion = "catholic"
    initial_culture = "english"
    initial_dynasty = create_dynasty(
        dynasties=dynasties, culture=initial_culture)
    dynasties.add(initial_dynasty)
    initial_character = create_character(names=names, characters=characters, dynasty=initial_dynasty, religion=initial_religion,
                                         culture=initial_culture, id=initial_id, father_id=initial_id-1, mother_id=initial_id-1)
    characters.add(initial_character)
    return {
        "dynasties": dynasties,
        "characters": characters
    }


def main():
    names = []
    with open("names.txt", "r") as names_file:
        names = [name.strip() for name in names_file.readlines()]
    initial_dict = initialize(names=names)
    print(initial_dict)


if __name__ == '__main__':
    main()
