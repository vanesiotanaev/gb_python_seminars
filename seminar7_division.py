num1 = 0
num2 = 0
operationName = 'division'

def init(a, b):
    global num1
    global num2
    num1 = a
    num2 = b

def operation():
    return num1 / num2 if num2 != 0 else 'Деление на ноль!'