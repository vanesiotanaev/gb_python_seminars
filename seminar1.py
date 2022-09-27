# #1. Напишите программу, которая принимает на вход 
# # два числа и проверяет, является ли одно число 
# # квадратом другого.

# print("Введите первое число:")
# a = int(input())
# print("Введите второе число:")
# b = int(input())

# if a**2 == b:
#     print(f"{b} -- квадрат числа {a}!")
# elif b**2 == a:
#     print(f"{a} -- квадрат числа {b}!")
# else:
#     print("Ни одно из этих двух чисел не является квадратом другого!")


# #2. Напишите программу, которая на вход принимает 
# # 5 чисел и находит максимальное из них.

# print("Введите первое число:")
# c = int(input())
# print("Введите второе число:")
# d = int(input())
# print("Введите третье число:")
# e = int(input())
# print("Введите четвертое число:")
# f = int(input())
# print("Введите пятое число:")
# g = int(input())

# numbers = [c, d, e, f, g]
# max = numbers[0]
# for i in numbers:
#     if i >= max:
#         max = i
# print(f"{max} -- максимальное число из данного списка: {numbers}")

# #Альтернативное решение
# numbers = []
# for i in range(0, 5):
#     numbers.append(int(input(f'Введите {i+1}e число: ')))
# print(f'Массив из {len(numbers)} чисел выглядит так: {numbers}')
# for i in numbers:
#     if i >= max:
#         max = i
# print(f"{max} -- максимальное число из данного списка: {numbers}")

#Альтернативное решение

# def ListCreate(size):
#     numbers = []
#     for i in range(0, size):
#         numbers.append(float(input(f'Введите {i+1}e число: ')))
#     print(f'Список из {len(numbers)} чисел выглядит так: {numbers}')
#     max = numbers[0]
    
#     for i in numbers:
#         if i >= max:
#             max = i
#     return max

# max_value = ListCreate(5)
# print(f"{max_value} -- максимальное число из данного списка")

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# def ShowValuesNToN (n):
#     values = []
#     for i in range(-n, n+1):
#         values.append(i)
    
#     return values

# numbers = ShowValuesNToN(int(input("Введите число N: ")))
# print(f"Список от {numbers[0]} до {numbers[len(numbers) - 1]} выглядит так: {numbers}")

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# def ShowFractionNumber (value):
#     if value % 1 == 0:
#         print(f"Число {int(value)} не является дробным")
#     else:
#         value = int((value*10)%10)
#         print (f"Цифра {value} -- первая по счету в дробной части введенного числа.")
#     return value

# a = ShowFractionNumber(float(input("Введите число: ")))

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

def Divisibility (value):
    if (value % 15 == 0 or (value % 10 == 0 and value % 5 == 0)) and not value % 30 == 0 :
        print (f"Число {value} кратно 5 и 10 или 15, но не 30!")

        return True
    else:
        print (f"Число {value} кратно 30!")
        return False

cond = Divisibility(int(input("Введите число: ")))