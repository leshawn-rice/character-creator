import random
from character import Character
from dynasty import Dynasty


class Generator(object):
    def __init__(self, culture: str = "english", religion: str = "catholic", initial_character_id: int = 1, character_names: list = [], can_inherit_name: bool = False):
        self.initial_culture = culture
        self.initial_relgion = religion
        self.culture = self.initial_culture
        self.religion = self.initial_religion
        self.dynasties = set()
        self.characters = set()
        self.character_id = initial_character_id
        self.character_names = character_names
        self.can_inherit_name = can_inherit_name

    def randomize_attributes(self):
        new_dynasty = False
        new_culture = False
        dynasty_chance = random.randint(1, 10)
        if dynasty_chance == 10:
            new_dynasty = True
        culture_chance = random.randint(1, 10)
        if culture_chance >= 7:
            new_culture = True
        if new_culture:
            self.create_culture()
        if new_dynasty:
            self.create_dynasty()

    def fix_naming_conflicts(self, character: Character = None) -> Character:
        named_character = Character.find(
            characters=self.characters,
            name=character.name
        )
        # no naming conflict
        if not named_character:
            return character

        while named_character:
            # if name matches a sibling, or parent and cannot match parent
            if named_character.is_sibling(character) or (named_character.is_parent(character) and not self.can_inherit_name):
                # give char new name
                character.name = random.choice(self.character_names)
                # find named_character
                named_character = Character.find(
                    characters=self.characters,
                    name=character.name
                )
            else:
                named_character = None
        return character

    def create_culture(self):
        name = random.choice(["one", "two", "three"])
        self.culture = name

    def create_dynasty(self):
        name = random.choice(["one", "two", "three"])
        id = self.dynasty.id + 1
        self.dynasty = Dynasty(id=id, name=name, culture=self.culture)

    def create_character(self, father_id: int = 1, mother_id: int = 1, birth_date: str = "01.01.0001", death_date: str = None) -> Character:
        name = random.choice(self.character_names)
        self.randomize_attributes()
        character = Character(
            id=self.character_id,
            dynasty=self.dynasty,
            name=name,
            religion=self.religion,
            culture=self.culture,
            father_id=father_id,
            mother_id=mother_id,
            birth_date=birth_date,
            death_date=death_date
        )
        character = self.fix_naming_conflicts(character)
        self.character_id += 1
        return character
