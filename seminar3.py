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