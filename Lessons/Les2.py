#Тема №2. OOП 2: Принцип ООП - Наследование, Полиморфизм

from Les1 import Car, mers

class Factory():
    name = 'organ'
    def __init__(self, id):
        self.id = id


class BMW(Car, Factory):
    name = 'BMW'

    def __init__(self, model, year, id):
        super().__init__(model, year)
        # Car.__init__(self, model, year) #На случай если множественное наследование
        Factory.__init__(self, id)

    def marks(self):
        print(f'Official bmw')

bmw = BMW('X5', 2007, 1)

bmw.marks()
bmw.sayname()

BMW.marks(mers)