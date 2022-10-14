import seminar7_view
import seminar7_multiplication
import seminar7_division
import seminar7_sum
import seminar7_difference
import seminar7_log

def button_click():
    value_a = seminar7_view.getValue() # Метод получения значений из view
    value_b = seminar7_view.getValue()
    operationName = seminar7_view.getOperationName()
    result = getOperation(value_a, value_b, operationName)
    seminar7_view.view(result, operationName)
    seminar7_log.log(result, operationName)

def getOperation(value_a, value_b, operationName):
    match operationName:
        case '+':
            seminar7_sum.init(value_a, value_b)
            return seminar7_sum.operation()
        case '-':
            seminar7_difference.init(value_a, value_b)
            return seminar7_difference.operation()
        case '*':
            seminar7_multiplication.init(value_a, value_b)
            return seminar7_multiplication.operation()
        case '/':
            seminar7_division.init(value_a, value_b)
            return seminar7_division.operation()
