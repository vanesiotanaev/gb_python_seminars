# Работа с выражениями (через строки)

# a = '1 - 5 * 2 / 2 * 3'
# print(a)
# a = a.split()
# print(a)

# while '*' in a or "/" in a and len(a) > 1:
#     for i in range(len(a)):
#         if a[i] == '*' or a[i] == '/':
#             if a[i] == '*':
#                 a[i - 1] = int(a[i - 1]) * int(a[i + 1])
#                 del a[i:i+2]
#                 print(' '.join(map(str, a))) # Перевожу поэлементно список 'a' в str.
#                 break
#             if a[i] == '/':
#                 a[i - 1] = int(a[i - 1]) / int(a[i + 1])
#                 del a[i:i+2]
#                 print(' '.join(map(str, a)))
#                 break
# while ('+' in a or '-' in a) and len(a) > 1:
#     for i in range(len(a)):
#         if a[i] == '+' or a[i] == '-':
#             if a[i] == '+':
#                 a[i-1] = int(a[i-1]) + int(a[i+1])
#                 del a[i:i+2]
#                 print(' '.join(map(str, a)))
#                 break
#             if a[i] == '-':
#                 a[i-1] = int(a[i-1]) - int(a[i+1])
#                 del a[i:i+2]
#                 print(' '.join(map(str, a)))
#                 break

# Работа с выражениями (через словари)

a = '1 - 5 * 2 / 2 * 3'
print(a)
math_ops = {'*': lambda x, y: int(x) * int(y),
            '/': lambda x, y: int(x) / int(y),
            '+': lambda x, y: int(x) + int(y),
            '-': lambda x, y: int(x) - int(y)}

a = a.replace(' ', '').strip()
a = a.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')
a = list(a.split())
print(a)

for i in range(len(a)):
    print(a[i])
    if a[i] in math_ops.keys() and a[i] == '*':       
        a[i - 1] = math_ops.get(a[i])(int(a[i-1]), int(a[i+1]))
        del a[i: i+2]
        print(a)
    elif a[i] in math_ops.keys() and a[i] == '/':
        a[i - 1] = math_ops.get(a[i])(int(a[i-1]), int(a[i+1]))
        print(a[i])
        del a[i: i+2]
        print(a)