
#19 – Наследование, инкапсуляция, полиморфизм
class Techno:
    name = None
    year = None
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def get_info(self):
        print("Techno Name:", self.name, "Year", self.year)


class Car(Techno):
    awd = True
    def __init__(self,name, year, awd):
        super().__init__(name, year)
        self.awd = awd

    def get_info(self):
        print("Car Name:", self.name, "Year:", self.year, "All Wheel Drive:", self.awd)

class Plane(Techno):
    maxSpeed = 2000
    def __init__(self, name, year, maxSpeed):
        super().__init__(name, year)
        self.maxSpeed = maxSpeed
    def get_info(self):
        print("Plane Name:", self.name, "Year:", self.year, "Max Speed:", self.maxSpeed)

class Bike(Techno):
    country = "Italy"
    def __init__(self, name, year, country):
        super().__init__(name, year)
        self.country = country
    def get_info(self):
        print("Bike Name:", self.name, "Year:", self.year, "Country:", self.country)
car = Car( "Audi", 1999, True)
car.get_info()
plane = Plane("Airbus", 2010, 2000)
plane.get_info()
bike = Bike("Ducati", 2025, "Italy")
bike.get_info()
# plane = Plane(Techno)
# plane.get_info()
# print(plane2.get_info())
# print(plane2.year)
#18 – Конструкторы, переопределение методов
# class Cars:
#     name = "Audi"
#     price = "$20000"
#     power = 500
#     def __init__(self, name, price, power):
#         self.name = name
#         self.price = price
#         self.power = power
#     def set_data(self, name, price, power):...
#
#     def get_data(self):...


# car1 = Cars("Audi", 20000, 500)
# car2 = Cars("BMW", 30000, 600)

#17 – Основы ООП. Создание класса и объекта
# class Person:
#     name  = None
#     age = None
#     isMale = True
#
#     def self_data(self, name, age, isMale):
#         self.name = name
#         self.age = age
#         self.isMale = isMale
#     def get_data(self, name, age, isMale):
#         print(self.name, "age:", self.age, "isMale: ",self.isMale)

# personSelf = Person()
# personSelf.self_data('Red', 26, True)
# personSelf.self_data('John', 26, True)
# personSelf.get_data('John', 26, True)
# print(personSelf.name)
# print(personSelf.age)
# person1 = Person()
# person1.name = "Dan"
# person1.age = 20
# person1.isMale = True
# print(person1.name)
# print(person1.age)
#
#
# person2 = Person()
# person2.name = "Victoria"
# person2.age = 30
# person2.isMale = False
# print(person2.name)
# print(person2)

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
