#
#
# country_counter = {}
#
# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#     else:
#         country_counter[country] = 1
#
# addone('China')
# addone('Japan')
# addone('china')
#
# print(len(country_counter))

# names1 = ['Amir', 'Barry', 'Chales', 'Dao']
# names2 = names1
# names3 = names1[:]
#
# names2[0] = "Alice"
# names3[1] = 'Bob'
#
# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#         sum += 1
#     if ls[1] == 'Bob':
#         sum += 10
# #
# print(sum)

# a = [1, 2, 3, None, (), [],]
# print(len(a))

# print(type([1, 2]))
#
# names1 = ['Amir', 'Barry', 'Chales', 'Dao']
# loc = names1.index("Edward")
# print(loc)
#
# name="SoftServe IT Academy"
# print(name.replace("o", "Q"))

# my_tuple = (1, 2, 3, 4)
# my_tuple.append( (5, 6, 7))
# print(len(my_tuple))
#
# name="SoftServe IT Academy"
# print(name.title())

# def parse_number(num):
#     count_of_odd = 0
#
#     count_of_even = 0
#     try:
#         for i in str(num):
#             if int(i)%2 == 0:
#                 count_of_even += 1
#             else:
#                 count_of_odd += 1
#
#         return {'odd': count_of_odd, 'even': count_of_even}
#     except ValueError:
#         return False
#     except TypeError:
#         return False
#
# print(parse_number(34567))
# print(parse_number(100))
# print(parse_number("word"))

# names1 = ['Amir', 'Barry', 'Chales', 'Dao']
#
# if 'amir' in names1:
#     print(1)
# else:
#     print(2)

# foo = (3, 4, 5)
# print(type(foo))

# print(0xA + 0xa)

# foo = {1: '1', 2: '2', 3: '3'}
# foo = {}
# print(len(foo))

# def f(): pass
# print(type(f()))
#
# x = True
# y = False
# z = False
#
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or not y and x:
#     print(3)
# else:
#     print(4)

# names1 = ['Amir', 'Barry', 'Chales', 'Dao']
# print("\n".join(names1))

# x = 5
# foo = x +=2
# print(foo)

# def a(b, c, d):
#     pass

# d = lambda p: p * 2
# t = lambda p: p * 3
# x = 2
# x = d(x)
# x = t(x)
# x = d(x)
# print(x)

# class Account:
#     def __init__(self, id):
#         self.id = id
#         id = 666
#
# acc = Account(123)
# print(acc.id)

# list_value = [None, 3, None, 5, None, None, 14]
# print(f"The origin list: {list_value}")
# res = [i for i in range(len(list_value)) if list_value[i] == None]
# print(f"The None index list is: {res}")

# nums = set([1, 1, 2, 3, 3, 3, 4])
# print(len(nums))

# class Person:
#     def __init__(self, id):
#         self.id = id
#
# obama = Person(100)
# obama.__dict__['age'] = 49
# print(obama.age + len(obama.__dict__))

# numberGames = {}
# numberGames[(1, 2, 4)] = 8
# numberGames[(4, 2, 1)] = 10
# numberGames[(1, 2)] = 12
#
# sum = 0
# for k in numberGames:
#     sum += numberGames[k]
# print(len(numberGames) + sum)
# #
# result = (80 - 12*5) / 4
# print(result)

# def findMaxSum(list_first):
#     maximum = 0
#     for x in list_first:
#         maximum = max(sum(x), maximum)
#     return maximum
#
# list_first = [[11, 2, 3], [44, 5, 6], [10, 1, 2], [17, 8, 6]]
# print("The max bla bla:", findMaxSum(list_first))

# kvps = {'1': 1, '2': 2}
# theCopy = dict(kvps)
#
# kvps['1'] = 5
#
# sum = kvps['1'] + theCopy['1']
# print(sum)

# def dostuff(param1, **param2):
#     print(type(param2))
#
#
# dostuff('capitals', Arizona='Phoenix',
#                     California='Sacramento',
#                     Texas='Austin')

# class Parent:
#     def __init__(self, param):
#         self.v1 = param
#
# class Child(Parent):
#      def __init__(self, param):
#          self.v2 = param
#
# obj = Child(11)
# print(obj.v1 + " " + obj.v2)

# x = True
# y = False
# z = False
#
# if x or y and z:
#     print("yes")
# else:
#     print("no")

# print(0.1 + 0.2 == 0.3)

# aList = [1, 2]
# bList = [3, 4]
#
# kvps = {'1': aList, '2': bList}
# theCopy = kvps.copy()
#
# kvps['1'][0] = 5
# sum = kvps['1'][0] + theCopy['1'][0]
# print(sum)

# boxes = {}
# jars = {}
# crates = {}
#
# boxes['cereal'] = 1
# boxes['candy'] = 2
# jars['honey'] = 4
# crates['boxes'] = boxes
# crates['jars'] = jars
#
# print(len(crates[boxes]))

# def print_header(str):
#     print("+++" + str + "+++")
#
# category = 1
# text = "some info"
#
# print_header("{} and {}".format(category, text))

# def myfunc(x, y, z, a):
#     print(x + y)
#
# nums = [1, 2, 3, 4]
#
# myfunc(*nums)

# names1 = ['Amir', 'Barry', 'Chales', 'Dao']
# names2 = [name.lower() for name in names1]
#
# print(names2[2][0])

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
#
# print(len(list1 + list2))

# numbers = [1, 2, 3, 4]
#
# numbers.append([5, 6, 7, 8])
#
# print(len(numbers))

# x = 4.5
# y = 2
# print(x//y)

# name = "snow storm"
# print(name[6:8])

# x = "foo"
# y = 2
# print(x + y)

# print("\x48\x49!")

# print(type(1/2))

# foo = {}
# print(type(foo))

# print(type([1,2]))

# one = chr(104)
# two = chr(105)
# print(one + two)
#
# name = "SoftServe IT  Academy"
# print(name.find("IT"))

# counter = 1
#
# def doLotsOf():
#
#     global counter
#     for i in (1, 2, 3):
#         counter += 1
# doLotsOf()
#
# print(counter)
#
# foo = {1 : '1', 2 : '2', 3 : '3'}
# del foo[1]
# foo[1] = '10'
# del foo[2]
# print(len(foo))

# print(type(1J))

# def addItem(listParam):
#     listParam += [1]
#
# mylist = [1, 2, 3, 4,]
# addItem(mylist)
# print(len(mylist))