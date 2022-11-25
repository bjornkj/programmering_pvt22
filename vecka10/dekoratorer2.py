import time
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

def timeit(func):
    def inner(a, b):
        start_time = time.time()
        result = func(a, b)
        print(f"tog {time.time() - start_time} sekunder")
        return result
    return inner


@timeit
def slow_add_function(a, b):
    time.sleep(2)
    return a + b



if __name__ == '__main__':
    print(slow_add_function(2, 2))
