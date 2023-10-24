class Individual:
    def __init__(self, x_array):
        self.x = x_array
        self.adaptation = None

    def __str__(self):
        return f"x_array: {self.x}, adaptation: {self.adaptation}"