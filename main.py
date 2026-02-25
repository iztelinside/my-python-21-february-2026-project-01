#17 – Основы ООП. Создание класса и объекта
class Person:
    name  = None
    age = None
    isMale = True

    def self_data(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale
    def get_data(self, name, age, isMale):
        print(self.name, "age:", self.age, "isMale: ",self.isMale)

personSelf = Person()
personSelf.self_data('Red', 26, True)
personSelf.self_data('John', 26, True)
personSelf.get_data('John', 26, True)
print(personSelf.name)
print(personSelf.age)
person1 = Person()
person1.name = "Dan"
person1.age = 20
person1.isMale = True
print(person1.name)
print(person1.age)


person2 = Person()
person2.name = "Victoria"
person2.age = 30
person2.isMale = False
print(person2.name)
print(person2)

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


# module

# import datetime as dt
# print(dt.datetime.today())
# print(dt.datetime.now().time())
# print(dt.datetime.now())
#
# from math import sqrt as sq
# from math import pi as pi
# print(sq(2))
# print(pi)
# def createWorst(elementOne, elementTwo):
#     print("Hello " + elementOne + " " + elementTwo)


# createWorst(elementOne="John", elementTwo="Black")
#
# def sumExam(elOne, elTwo, elThree, elFour):
#     res = elOne + elTwo + elThree+ elFour
#     return res
#
# print(sumExam(0, 5.5, 6.5, 10))
#
#
# numbers = [10, 90, 5, 39, -6, 67, 100, 400]
# min = numbers[0]
# for number in numbers:
#     if number < min:
#         min = number
#
# print(min)
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
