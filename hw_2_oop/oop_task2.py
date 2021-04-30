"""
2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
  a.
      class Person:
             Make the class with composition.
        class Arm:
           Make the class with composition.
  b.
      class CellPhone:
           Make the class with aggregation
      class Screen:
          Make the class with aggregation
 """


class Person:
    def __init__(self):
        left_arm = Arm('Position number five')
        right_arm = Arm('Position number seven')
        self.arms = [left_arm, right_arm]


class Arm:
    def __init__(self, position):
        self.position = position


print("Task 2.a")
person = Person()
for arm in person.arms:
    print(arm.position)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, diag="5.7"):
        self.diag = diag


print("Task 2.b")
screen = Screen()
phone = CellPhone(screen)
print(phone.screen.diag)






