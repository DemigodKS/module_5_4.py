class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):

        cls.houses_history.append(args[0])

        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name} кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Бобры', 15)
print(House.houses_history)

h2 = House('Домик в горах',5)
print(House.houses_history)

h3 = House('ЖК Лес', 2)
print(House.houses_history)

del h1
del h2

print(House.houses_history)








