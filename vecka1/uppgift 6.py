# Uppgift 6:

# 6.1 Få igång programmet d.v.s få till indenteringen och lägg till mellanrum där det känns vettigt t.ex. mellan funktioner
# 6.2 Subtraktion funkar inte (testa!). Rätta felet.
# 6.3 Multiplikation och division är inte färdigt, bara funktionerna finns. Utöka programmet så att alla fyra räknesätten finns med.

def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a + b
    return result


def multiply(a, b):
    result = a + b
    return result


def divide(a, b):
    result = a + b
    return result


def run():
    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    answer = input(">> ")
    a = int(input("A="))
    b = int(input("B="))

    if answer == "1":
        result = add(a, b)

    if answer == "2":
        result = subtract(a, b)

    print("Result = " + str(result))

if __name__ == '__main__':
    run()