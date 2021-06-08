class Pizza:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @classmethod
    def margarita(self):
        margar = Pizza('Margarita', ['mozarella', 'tomatos', 'olives'])
        return margar

    @staticmethod
    def calculate_area(radius):
        area = 3.14*radius**2
        return area

marg = Pizza.margarita()
print(marg.calculate_area(50))