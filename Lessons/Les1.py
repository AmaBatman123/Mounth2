# OOП 1: Основы ООП, Создание первых классов, Атрибуты и Методы классов, Принцип ООП - Наследование.

class Car:
    name = 'MERS'

    def __init__(self, model, year):
        self.model = model
        self.year = year


    # Метод вызова имени
    def sayname(self):
        print(f'{self.name} {self.model} {self.year}')

    def __str__(self):
        return (f'{self.name} {self.year}')

    def __len__(self):
        return len(self.model) + len(str(self.year))

mers = Car('E390', 1999)
mers2 = Car('C1050', 2003)

mers.sayname()
mers2.sayname()

print(len(mers2))
