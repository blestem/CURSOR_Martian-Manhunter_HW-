from abc import ABC, abstractmethod
import random


class Person(ABC):
    def __init__(self, name: str, age: int, money: (int, float), house: list = []):
        self.name = name
        self.age = age
        self.available_money = money
        self.own_home = house

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError


class Human(Person, ABC):
    def __init__(self, name: str, age: int, money: (int, float), house: list = []):
        super().__init__(name, age, money, house)
        self.salary = random.randint(5000, 15000)

    def info(self):
        print(f'Hello! My name is {self.name}, and I am {self.age} years old.')

    def make_money(self):
        self.available_money += self.salary

    def buy_house(self, house):

        if house.area >= 150:
            print('This house is too big for me. Maybe you have other suggestions?')
        elif house.cost >= self.available_money:
            print(f'{self.name} does not have enough money to buy this house.')
        elif realtor.steal_money() <= 10:
            self.available_money -= house.cost
            print(f'{realtor.name} turned out to be a thief and stole my money')
        else:
            self.available_money -= house.cost
            print(f'Congratulations to {self.name} on buying a house')

        return self.own_home.append(house)


class Building(ABC):
    def __init__(self, area: (float, int), cost: int):
        self.area = area
        self.cost = cost

    @abstractmethod
    def apply_discount(self):
        raise NotImplementedError


class House(Building):
    def __init__(self, area, cost):
        super().__init__(area, cost)

    def apply_discount(self, discount):
        self.cost -= (self.cost * discount)
        return self.cost


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name: str, discount: (float, int), houses: list = []):
        self.name = name
        self.discount = discount
        self.houses = houses

    def info_houses(self):
        if self.houses:
            print(f'Hello! My name is {self.name} and I am your realtor.')
            for house in self.houses:
                print(f' Now we have these houses for sale: \t{house}')
        else:
            print('We have not available hoses')
        return self.houses

    def give_discount(self):
        return self.discount

    def steal_money(self):
        return random.randrange(0, 100)

    def sold_house(self, house):
        self.houses.remove(house)


if __name__ == '__main__':
    house1 = House(40, 15000)
    house2 = House(165, 60000)
    house3 = House(150, 20000)

    realtor = Realtor('Jan', 0.20, [house1, house2, house3])
    person = Human('Anna', 34, 20000)

    person.info()
    person.make_money()
    realtor.info_houses()
    person.buy_house(house2)
    realtor.info_houses()
    person.buy_house(house3)
    realtor.info_houses()
    person.buy_house(house1)
    realtor.give_discount()
    realtor.sold_house(house1)
    realtor.info_houses()




