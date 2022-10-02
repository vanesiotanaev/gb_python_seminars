# Варианты решения 2 д.з.

# num = input("Введите вещественное число: ")
# sum = 0

# for item in num:
#     if item.isdigit():
#         sum += int(item)

# print(sum)

# Как сделать нормальную переменную с плавающей точкой

# def float_to_int(value):
#     multiplier = 1
#     float_value = value
#     while not float_value.is_integer():
#         multiplier *= 10
#         float_value = value * multiplier
    
#     return float_value

# def get_digits_sum(any_number):
#     no_point_value = float_to_int(any_number)
#     no_point_value = abs(int(no_point_value))
#     sum = 0
#     while no_point_value>0:
#         sum += int(no_point_value % 10)
#         no_point_value /= 10
    
#     return sum

# user_value = float(input("Enter the float-value: "))
# mod_user_value = float_to_int(user_value)
# print(int(mod_user_value))
# sum_value_nums = get_digits_sum(mod_user_value)
# print(sum_value_nums)

# Напишите программу, которая определит, присутствует ли в заданном списке строк искомое число.
# Если присутствует, то в каком элементе?

# def find_value(list, value):
#     new_list = []
#     for item in list:
#         if str(value) in item:
#             new_list.append(list.index(item))
#     if len(new_list) > 0:
#         return new_list
#     else:
#         print("Введенное значение отсутствует в списке")

# user_list = ['abfg,', 'gg7ha', 'koa123', 'Gh700', 'fdgd']
# user_num = int(input('Enter the number you want to find: '))
# print(find_value(user_list, user_num))

# Напишите программу, которая определит позицию второго вхождения
# строки в список, либо сообщит, что ее нет:

def find_2nd_entrance(list, text):
    count = 0
    for i in range(0, len(list)):
        if str(text) in str(list[i]):
            count += 1
        if count == 2:
            print(f'Второе вхождение строки "{text}" в список {list} находится по индексу {i}')
            return i
    else:
        print("Второго вхождения введенного текста в список нет!")

user_list = ['abc,', 123, 'asd', 'пщпщп,', 123, 'abc,', 'fло1', 'asd']
user_text = (input('Enter the string you want to find: '))
find_2nd_entrance(user_list, user_text)
