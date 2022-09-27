#1. Напишите программу, которая принимает на вход 
# два числа и проверяет, является ли одно число 
# квадратом другого.

print("Введите первое число:")
a = int(input())
print("Введите второе число:")
b = int(input())

if a**2 == b:
    print(f"{b} -- квадрат числа {a}!")
elif b**2 == a:
    print(f"{a} -- квадрат числа {b}!")
else:
    print("Ни одно из этих двух чисел не является квадратом другого!")


#2. Напишите программу, которая на вход принимает 
# 5 чисел и находит максимальное из них.

print("Введите первое число:")
c = int(input())
print("Введите второе число:")
d = int(input())
print("Введите третье число:")
e = int(input())
print("Введите четвертое число:")
f = int(input())
print("Введите пятое число:")
g = int(input())

numbers = [c, d, e, f, g]
max = numbers[0]
for i in numbers:
    if i >= max:
        max = i
print(f"{max} -- максимальное число из данного списка: {numbers}")

#Альтернативное решение
numbers = []
for i in range(0, 5):
    numbers.append(int(input(f'Введите {i+1}e число: ')))
print(f'Массив из {len(numbers)} чисел выглядит так: {numbers}')
for i in numbers:
    if i >= max:
        max = i
print(f"{max} -- максимальное число из данного списка: {numbers}")
