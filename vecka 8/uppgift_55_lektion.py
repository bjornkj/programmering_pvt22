def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    result = a / b
    return result


operations = {"1": add,
              "2": subtract,
              "3": multiply,
              "4": divide}


def run():
    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    print("3 - multiply numbers")
    print("4 - divide numbers")

    answer = input(">> ")
    a = int(input("A="))
    b = int(input("B="))

    result = operations[answer](a, b)
    print("Result = " + str(result))

if __name__ == '__main__':
    run()

