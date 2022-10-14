import datetime

path = 'seminar7_log.txt'

def log(result, operationName):
    string = f'{datetime.datetime.now()}: {result}'
    with open(path, 'a', encoding='utf_8') as data:
        data.write(f'{string}\n')