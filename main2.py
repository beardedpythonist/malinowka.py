# import requests
#
# response = requests.options('http://google.com')
# zapros = requests.get(url='http://onliner.by', method="GET")
#
#
# print(response.headers)
#
#
# for key, val in response.headers.items():
#      print(f' ключ:  {key}, значение: {val}')
#
# import os
# print('тек директория', os.getcwd())
#
#
# os.chdir('папка')
#
#
# print('тек директория', os.getcwd())
#
#
# os.chdir('..')
# os.chdir('..')
# os.chdir('..')
# print('тек директория', os.getcwd())


#
# def hide_card(card):
#     card_def = card.replace(' ', '')
#     zwesd = '************'
#     card_new = zwesd + card_def[-4:]
#     return card_new

# numbers  = [6, 0, 67, -7, 10, -20]
#
# def same_parity(numbers):
#     if numbers == []:
#         return []
#     if numbers[0] % 2 == 0:
#         f = lambda x:  x % 2 == 0
#         numbers = list(filter(f, numbers))
#         return numbers
#     else:
#         f1 = lambda x: x % 2 == 1
#         numbers = list(filter(f1, numbers))
#         return numbers
# print(same_parity(numbers))
#
#
# pin = '123fvdfgf456'
# def is_valid(string):
#     flag = True
#     return flag if string.isnumeric() and 4 <= len(string) <= 6 and ' ' not in string else False
#
# dict1  = {'Вася': 25,'Коля': 30, 'Зина': 20 }
# dict1 = sorted(dict1)
# print(dict1)
#
# Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов и выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая на отдельной строке, в следующем формате:
#
# для позиционных аргументов:
# <значение аргумента> <тип аргумента>
# для именованных аргументов:
# <имя переменной> <значение аргумента> <тип аргумента>


# def print_given(*args, **kwargs):
#     for c in range(len(args)):
#         print(args[c], type(args[c]))
#
#     for key, val in sorted(kwargs.items()):
#         print(key, val , type(val))
#
# #
# print_given(b=2, d=4, c=3, a=1)


#
# def convert(string):
#     count_small = 0
#     count_big = 0
#     for c in string:
#         if c.islower():
#             count_small += 1
#         elif c.isupper():
#             count_big += 1
#     if count_big == count_small:
#         string = string.lower()
#     if count_small > count_big:
#         string = string.lower()
#     if count_big > count_small:
#         string = string.upper()
#
#     return string
#
#
# print(convert('ABCees'))

 # пример на словари  на подсчет символов
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
#
# result = {}
# for s in text:
#     result[s] = result.get(s, 0) + 1
#
# print(result)



# Анаграммы — это слова, которые состоят из одинаковых букв. Например:
#
# адаптер — петарда
# адресочек — середочка
# азбука — базука
# аистенок — осетинка
# Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
#
# word — слово в нижнем регистре
# words — список слов в нижнем регистре
# Функция должна возвращать список, элементами которого являются слова
# из списка words, которые представляют анаграмму слова word. Если список
# words пуст или не содержит анаграмм, функция должна вернуть пустой список.
# def filter_anagrams(word, words):
#     anagrams = words
#     count_1 = 0
#     for c in word:
#         count_1 = count_1 + ord(c)
#     list_final = []
#     for c in anagrams:
#         count2 = 0
#         for q in c:
#             count2 = count2 + ord(q)
#         if count_1 == count2:
#             list_final.append(c)
# #     return list_final
#
# ls1 = []
# def likes(names):
#     ls1 = names
#     if len(ls1) == 0:
#         return 'Никто не оценил данную запись'
#     elif len(ls1) == 1:
#          return  f'{ls1[0]} оценил(а) данную запись'
#     elif len(ls1) == 2:
#         return f' {ls1[0]} и {ls1[1]} оценили данную запись'
#     elif len(ls1) == 3:
#         return f' {ls1[0]}, {ls1[1]} и {ls1[2]} оценили данную запись'
#
#     elif len(ls1) >= 4:
#         return  f' {ls1[0]}, {ls1[1]} и {len(ls1[2:])} оценили данную запись'
#
# print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
#
# фактариал
# x = 5
# f =  1
# for c in range(1, x + 1):
#     f = f * c
# print(f)




