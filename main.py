
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

def simple_dec(func1):
    def wrapper():    # обернуть в wrapper
        print('Начало')
        func1()
        print('Конец')
    return  wrapper   # не забыть


@simple_dec
def func1():    # основаная фунция
    print('Privet')
func1()          # выздвать основную





