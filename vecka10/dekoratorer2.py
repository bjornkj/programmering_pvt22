
# Jag vill lägga till funktionalitet, före och efter ett funktionsanrop


def min_dekorator(func):
    def inner():
        print(f"Skall precis köra funktionen {func}")
        func()
        print("Klar")
    return inner


@min_dekorator # motsvarar foo = min_dekorator(foo)
def foo():
    print("Hej, jag är funktionen foo")

# Skapa en dekorator som tar tiden på en funktion
# kalla den för timeit
# om vi använder den så här
# @timeit
# def en_funktion():
#   gör något som tar tid
#
# så skall detta
# en_funktion()
# köra funktionen en_funktion, samt skriva ut tiden det tog
# Använd module time
#

if __name__ == '__main__':
    foo()
