class Item:
    def __init__(self, id, name, weight, value):
        self.id = id
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return f"{self.id} {self.name} {self.weight} {self.value}"
