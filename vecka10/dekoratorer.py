

def foo():
    print("Hej, jag är funktionen foo")


bar = foo

def function_runner(a):
    print(f"Hej jag är funktionen function runner, skall nu köra: {a}")
    a()
    print("Färdigt")


def create_adder(n: int): # Funktionen create_adder är som en maskin som kan tillverka nya funktioner
    def inner(a: int): # Skapar en ny funktion, som tar ett argument a
        return n+a
    return inner

# create_adder(2)
# Resulterar i följande
# def inner(a: int):
#   return 2+a

if __name__ == '__main__':
    function_runner(bar)

    add_2 = create_adder(2)
    add_100 = create_adder(100)
    print(add_2(1))
    print(add_100(5))
