class Dynasty():
    def __init__(self, id: int = 0, name: str = "Example", culture: str = "english"):
        self.id = id
        self.name = name
        self.culture = culture

    @classmethod
    def find(cls, dynasties: set = {}, name: str = 'Example'):
        for dynasty in dynasties:
            if dynasty.name == name:
                return dynasty

    def write(self, file=None):
        file.write(
            f"{self.id} = {{\n    name = \"{self.name}\"\n    culture = {self.culture}\n}}"
        )

    def __eq__(self, dynasty):
        if not dynasty:
            return False
        if not isinstance(dynasty, Dynasty):
            return False
        if dynasty.id != self.id or dynasty.name != self.name or dynasty.culture != self.culture:
            return False
        return True

    def __lt__(self, dynasty):
        if not dynasty or not isinstance(dynasty, Dynasty):
            raise TypeError(
                "'<' not supported between instances of 'Dynasty' and '{}'".format(
                    type(dynasty))
            )
        if self.id < dynasty.id:
            return True
        return False

    def __gt__(self, dynasty):
        if not dynasty or not isinstance(dynasty, Dynasty):
            raise TypeError(
                "'<' not supported between instances of 'Dynasty' and '{}'".format(
                    type(dynasty))
            )
        if self.id > dynasty.id:
            return True
        return False

    def __repr__(self):
        return f"<Dynasty #{self.id} {self.name}>"

    def __hash__(self):
        return hash(repr(self))
