"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class

class Animals:
    Parent class, should have eat, sleep
   class Animal1(Animal):
    Some of the animal with 1-2 extra methods related to this animal
"""


class Animals:
    def eat(self):
        print(f'{self.__class__.__name__} eating')

    def sleep(self):
        print(f'{self.__class__.__name__} sleeping')


class Cat(Animals):
    def catch_mice(self):
        print(f'{self.__class__.__name__} catch mice')


class Mantis(Animals):
    def jump(self):
        print(f'{self.__class__.__name__} jumping')


class Butterfly(Animals):
    def fly(self):
        print(f'{self.__class__.__name__} flying')


class Triton(Animals):
    def regenerate(self):
        print(f'{self.__class__.__name__} regenerating')


class Snake(Animals):
    def crawl(self):
        print(f'{self.__class__.__name__} crawling')


cat = Cat()
mantis = Mantis()
butterfly = Butterfly()
triton = Triton()
snake = Snake()

print('Task 1')
cat.sleep()
triton.regenerate()
mantis.eat()

print(f'cat is an instance of the Animals class: {isinstance(cat, Animals)}')
print(f'mantis is an instance of the Animals class: {isinstance(mantis, Animals)}')
print(f'butterfly is an instance of the Animals class: {isinstance(butterfly, Animals)}')
print(f'triton is an instance of the Animals class: {isinstance(triton, Animals)}')
print(f'snake is an instance of the Animals class: {isinstance(snake, Animals)}')


"""
 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.
 
 class Human:
    Human class, should have eat, sleep, study, work
 
 class Centaur(.. , ..):
    Centaur class should be inherited from Human and Animal and has unique method related to it.
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} eating')

    def sleep(self):
        print(f'{self.name} sleeping')

    def study(self):
        print(f'{self.name} studying')

    def work(self):
        print(f'{self.name} working')


class Centaur(Animals, Human):
    def predict_future(self):
        print(f'{self.name} tell the future')

    def archery(self):
        print(f'{self.name} archery')


centaur = Centaur('Magorian', 35)
print('Task 1.a')
centaur.eat()
centaur.sleep()
centaur.study()
centaur.predict_future()
