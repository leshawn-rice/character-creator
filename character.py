from dynasty import Dynasty


class Character():
    def __init__(self, id: int = 0, dynasty: Dynasty = None, name: str = "John", religion: str = "catholic", culture: str = "english", father_id: int = 0, mother_id: int = 0, birth_date: str = "0001.01.01", death_date: str = "0081.01.01"):
        self.id = id
        self.name = name
        self.dynasty = dynasty
        self.religion = religion
        self.culture = culture
        self.father_id = father_id
        self.mother_id = mother_id
        self.birth_date = birth_date
        self.death_date = death_date

    @classmethod
    def find(cls, characters: set = {}, name: str = "John"):
        for character in characters:
            if character.name == name:
                return character

    def is_sibling(self, character):
        return self.father_id == character.father_id or self.mother_id == character.mother_id

    def shares_father(self, character):
        return self.father_id == character.father_id

    def shares_mother(self, character):
        return self.mother_id == character.mother_id

    def shares_name(self, character):
        return self.name == character.name

    def is_parent(self, character):
        return self.id == character.father_id or self.id == character.mother_id

    def write(self, file=None):
        file.write(
            f"{self.id} = {{\n    # Character Attributes\n\n    name = \"{self.name}\"\n    dynasty = {self.dynasty.id}\n    religion = \"{self.religion}\"\n    culture = \"{self.culture}\"\n    father = {self.father_id}\n    mother = {self.mother_id}\n\n    # Character history\n\n    {self.birth_date} = {{\n        birth = yes\n    }}\n    {self.death_date}{{\n        death = yes\n    }}\n}},\n"
        )

    def __eq__(self, character):
        return self.id == character.id

    def __lt__(self, character):
        return self.id < character.id

    def __gt__(self, character):
        return self.id > character.id

    def __repr__(self):
        return f"<Character #{self.id} {self.name}>"

    def __hash__(self):
        return hash(repr(self))
