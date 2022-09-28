# Задача с предикатами, правильное решение

# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

# trigger = True

# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             if not (x or y or z) != (not x) and (not y) and (not z):
#                 print('Not True!')
#                 trigger = False
#                 break
# if trigger:
#     print ("Always True!")

# Нужные hints

# 1.

# a = 4
# b = a
# a += 5
# print(b)

# 2.

# a = [1, 2, 3]
# b = a
# a.append(4)
# print(b)

# b будет равно [1,2,3,4]
# Потому что сначала а ссылается на ячейку, в которой хранится массив из 3 элементов.
# Потом b начинает ссылаться на ту же ячейку, и продолжает на нее ссылаться всегда. 
# И, в отличие от случаев с переменными, если ячейку, на которую ссылаются a и b, изменяется,
# то изменяются и все, что на нее ссылается. Именно со списками так.

# 3. 

# Можно сделать копию ячейки.

# a = [1, 2, 3]
# c = a.copy()
# c.append(7)

# print(a)
# print(c)

# Тогда с уже ссыылается на копию ячейки, на которую ссылается а.
# Можно через "срез"
# a = [1,2,3]
# c = a[:]
# c.append(77)

# print(a)
# print(c)

# Class Work.

# 1. 
# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# def SpecialNValues(n):
#     values = []
#     value = 1
#     values.append(value)
#     for i in range (n-1):
#         value = value*3*(-1)
#         values.append(value)
#     return values

# user_value = int(input("Enter the N-number of values: "))
# print(SpecialNValues(user_value))

# 2. 
# Словари.

# dict = {}
# dict[1] = 'Вова'
# dict[78] = 'Боб'
# dict[4] = 'Jack'
# print(dict)

# list = []
# list.append(5)
# print(list)

# print(dict.get(3))
# print(dict.get(78))

# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def CreateSpecialDict(n):
#     dict = {}
#     for i in range(1, n+1):
#         dict[i] = 3*i+1
#     return dict

# user_number = int(input("Enter the N-number: "))
# user_dict = CreateSpecialDict(user_number)
# print(user_dict)

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа -
#  определять количество вхождений одной строки в другой.

def CountSimilarString(str1, str2):
    if len(str1) == len(str2):
        if str1 == str2:
            return 1
        else: 
            return 0
    elif len(str1) > len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] == str2[0]:
                if str1[i:i+len(str2)] == str2:
                    count += 1            
    else:
        count = 0
        for i in range(len(str2)):
            if str2[i] == str1[0]:
                if str2[i:i+len(str1)] == str1:
                    count += 1     
                    
    return count

string1 = str(input("Enter the 1st string: "))
string2 = str(input("Enter the 2nd string: "))
how_much = CountSimilarString(string1, string2)
print(f"Одна строка повторяет другую {how_much} раз(а).")      

# string.count(substring) -- готовый метод


