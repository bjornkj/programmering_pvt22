
import inspect

global_val = 10


def do_something(a, b):
    return (a + b) * global_val


def do_with_side_effect(a): # Den här funktionen kommer påverka saker utanför funktionen
    global global_val
    global_val += 1
    return global_val * a



# Funktionen skall ta ett tal n och en optional lista
# Ger som resultat talen 0-n i slutet på listan
# foo(5) -> [0, 1, 2, 3, 4, 5]
# foo(5, [-2, -1]) -> [-2, -1, 0, 1, 2, 3, 4, 5]
def foo(n, li=[]):
    for i in range(n+1):
        li.append(i)
    return li


if __name__ == '__main__':
    print(do_something(3, 2)) # 50, (3+2) * 10
    global_val += 1
    print(do_something(3, 2)) # 55, (3+2) * 11, vi har ökat värde på global_val med 1

    print(do_with_side_effect(10)) # Anropet till do_with_side_effect påverkar global_val, ökar med 1
    print(do_something(3, 2)) # 50, (3+2) * 12
    print("-"*80)

    print(foo(5, [-2, -1]))

    print(foo(5))
    print(foo(5))
    print(foo(5))
    print(foo(10, []))
    print(foo(2))