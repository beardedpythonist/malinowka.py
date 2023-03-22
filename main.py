# #1  просто перечсисляем
#
# slov1 = {'wasja': 27, 'zosja': 35}
# print(slov1)
#
#
# #2 фнк dict
# lis11 = [1,5,9,]
# slo2 = dict(hello = lis11)
# print(slo2)
#
#
# #3 fromkeys
# slo3  = dict.fromkeys(lis11, 'table')
# print(slo3)
#
#
# #4
# slo4 = {x ** 2:x for x in range(10)}
# print(slo4)
#
# #5
# d ={}
#
#
# #6 список из артежей
#
# dict6 =dict([('age', 25),('job', 'teacher'),('result', 'ok')])
# print(dict6)
#
# # 7   картежи списов
#
# dict7 =  dict((['age', 25],['result', 'bad'],['job', 'doctor']))
# print(dict7)
#
# #8
#


#
# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
# new_caps = capitals.copy()
# print(capitals)
#
# new_caps['RB'] = 'Minsk'
# capitals['UKR'] = 'KIew'
# print(capitals)
# print(new_caps)


# def summa(*args):
#     print(args)
#
#
# kart1=(1,5,9,22,2)
#
# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}
#
# summa(*kart1)


#
# numbers = {1, 1, 2, 3, 5, 8, 3}  # создаем множество
#
# numbers.add(25)

# сумма цифр

# n = int(input())
#
# sum = 0
# while  n > 0:
#     x = n % 10
#     sum += x
#     n = n // 10
# print(sum)


#  только положительные
#
# a, b, c = int(input()), int(input()), int(input())
#
# if a  > 0:
#     a1 =  a
# else:
#     a1 = 0
# if b  > 0:
#     b1 = b
# else:
#     b1 = 0
# if c > 0:
#     c1 = c
# else:
#     c1 = 0
#
# sum1 = a1 + b1 + c1
# print(sum1)
#

# class Car():
#     def __init__(self, model, year, price):
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def allprint(self):
#         print(self.year)
#
# BMW =  Car('E39', 2022, 15000)
# Audi = Car('A4', 2010, 2000)
# Audi.allprint()
#
#
#


#
# class Person:    # атрубут класса пример
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
#
# ob1 = Person('wasja')
# ob2 =  Person('Petja')
# ob3 = Person('kola')
# ob4 = Person
# ob4.name = 'Zina'
# print(ob4.name)
#


# декораторы
# 1 ) определяем декоратор
#
# def simple_dec(func1):
#     def wrapper():    # обернуть в wrapper
#         print('Начало')
#         func1()
#         print('Конец')
#     return  wrapper   # не забыть
#
#
# @simple_dec
# def func1():    # основаная фунция
#     print('Privet')
# func1()          # выздвать основную
#
#
# #
# import random
#
# color = ['white', 'black', 'red']
# year = [2002, 2010, 2015]
# model = ['BMW', "Audi", 'Opel', "MERC"]
# class  Car:
#     count = 0
#     def __init__(self, color, year, model):
#         Car.count += 1
#         self.color = color
#         self.year = year
#         self.model = model
#
#
#     def info_obj(self):
#         return self.color, self.year, self.model
#
#
#     @staticmethod
# def createobjects():
#     carlist = {}
#     for c in range(10):
#         color = random.choice(color)
#         year = random.choice(year)
#         model = random.choice(model)
#         object = Car(color, year, model)
#         print(object.info_obj())
#         carlist[object.model] = object.info_obj()
#     print(carlist)

#
# tup1 = (1, 2, 5, 7)
# x = sum(tup1)
#
# print(x)
#
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
#
# print(a == b)
# print(id(a))
# print(id(b))
#
# print(a is c)
# print(id(c))



# class Car:
#
#     def __init__(self, color, speed):
#
#         Car.count += 1
#         self.color = color
#         self.speed = speed
#
#     def info(self):
#         return  self.speed, self.color
#
#     @staticmethod
#     def create():
#         for c in range(5):
#             obj = Car('red', 150)
#             print(obj.info())
#
# Car.create()
# print(Car.count)


#
# def func():
#     print('Im a function')
#
#
# print(func)
# list1  = [10, 20 , 30, 50, 80]
#
#
# f = lambda x: x > 30
#
#
#
# list1 = list(filter(f, list1))
#
#
# print(list1)


# list1  = [10, 20 , 30, 50, 80]
# list1.reverse()
# print(list1)
#
#
#
# list_new = list1  * 3
# print(list_new)
#
#
# list1 = [10, 20, 30, 50, 80]
# list4 = list1.copy()
# print(list4)
#
# list1.append(77)
# print(list1)
#
# list1 = [10, 20, 30, 50, 80, 50, 20]
#
# list2 = list1[:2]
# print(list2)
# list3  = list1[2:]
# print(list3)
#
#
# set1  = set(list1)
# print(list(set1))
#
# slov1  = {'wasja': 25, 'petja': 30, 'zosja': 40, 'masha': 20}
#
#
# for key, val in sorted(slov1.items(), key=lambda x: x[1]):
#     print(key, val)
#
#
# biglist = [(1,3,5),(5,7,1),(1,6,9),(10,2,7)]
# listnew = sorted(biglist, key= lambda x : x[1])
#
# print(listnew)
#
# str1  = 'dsjklsdf sdfsdkl f sdklfsdlfkdlkflsk ldfs'
#
# lis1 = str1.split('f')
# print(lis1)
#
#
#
# list1 = [10, 20, 30, 50, 80, 50, 20]
#
# for c in range(len(list1)):
#     print(c, list1[c])
#

# простое число , команда break
#
# x  = int(input())
#
# flag =  True
#
#
# for c in range(2, x):
#     if x % c == 0:
#         flag = False
#         break
#
# print(flag)

#ример континю
# for i in range(10):
#     if i == 7:
#         continue
#     print(i)


#
#
# a = [1,2,3,4,5]
#
# a2 = []
# for i in a:
#      a2.append(i + 1)
# print(a2)
#
#
# a2 = [i + 1 for i in a]
# print(a2)
#
# Тернарный (условный) оператор — это однострочный оператор if/else.
#
# Синтаксис такой: a if condition else b.
# a = 101
#
# print('Privet' if a < 100 else 'poka')

#
# str1 = 'fdsffsdf323423423fsdsfdfsd'
# print(str1.isnumeric())

# d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
# spis = list(d)
#
# for key in d.keys():
#     print(key)
#
# str1 = 'fdsffsdf323423423fsdsfdfsd'.upper()
# print(str1)

#
# del, remove , pop примеры

# d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
# a = [1,2,3,4,5]
#
#
# a.pop()
#
# x = d.pop('name')
# print(d)
# print(a)


#
# str1  = 'dwwwrrr111444'
# str1 =(str1)
# print(str1)

# list1 = [1,2,3,4,5, 8, 10, 20]
# for c in range(len(list1) - 1, 0,  -1):
#     print(list1[c])

#
# ls = [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
#
#
# ls0 = [1, 2, 3]
# ls1 = [6]
# ls3 = [7, 8, 9, 10, 11, 12, 13]
# ls_final = ls0 + ls0 + ls1 * 6 + ls3
# print(ls_final)
# #
# На вход программе подается натуральное число
# �
# n. Напишите программу, которая создает список состоящий из делителей введенного числа.

# n  = int(input())
#
# ls = []
# for c in range(1, n+1):
#
#     if n % c == 0:
#         ls.append(c)
# print(*ls)
#
#
#
#
# вывести вертикально
#
# s = 'Python'
#
# print(*s)
# print()
# print(*s, sep='\n')

#
# str1 ='fd df ghfg 54 hgg'
# lis1  = str1.split()
# print(lis1)

# объединяет заняения списка в строку.
# ls2  = ['33', '46','67','567','68']
# str2  =  ''.join(ls2)
# print(str2)

# пример генератор словаря (можно и с ключами и с о значениями манипулировать)
# slov2 = {x ** 2: x  for x in range(10)}
# print(slov2)
#

# пример try - except

#
# try:
#     a  = 1 + '1'
# except:
#     print( 'числа и строки не складываются')
#
# finally:
#
#     print('poka')
#
#
# from decimal import *
# a = Decimal(0.3)
# b = Decimal(0.1) + Decimal(0.1) + Decimal(0.1)
# print(a == b)
#
# пример deepcopy
import copy
#
# str1 = 'ffdd1133'
# str2 =str1[::-1]
# print(str2)
#

import copy
#
# пример копии
# li1 = [['a'],['b'],['c']]
# li2 = li1.copy()
# print(li2)
# li1[0][0] = 'x'
# print(li2)

# пример локальной и глобальной функции
# def showname():
#     global x
#     x  = 30
#     print(x)
#
# showname()
#
# q =  x * 2
# print(q)

# ls1  = [1,54,7,9,0]
#
# print(ls1[-4:-2])
#
# def fun0(*args):
#    print(min(args))
#
# fun0(5,9,10)

#
# def fun1(**kwargs):
#    print(kwargs)
#
# fun1(x=5, y=8, z=10)


# def privet(showname):
#    def wrapper():
#       print('Wasje privet')
#       showname()
#       print('Poka')
#    return wrapper
#
#
# @privet
# def showname():
#    print('Ja Wasja')
#
# showname()


# пример private метода  и инкомпусляции
# class Car:
#    def __init__(self, model, price):
#       self.model = model
#       self.__price = price
#
#
# ob1 = Car('BMW', 15000)
# print(ob1.price)

