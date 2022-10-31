

def my_func(a, b=10):
    return a+b


def func2(a):
    return a*a


if __name__ == '__main__':
    print(my_func(5))
    print(my_func(5, 2))

    print(my_func)
    print(type(my_func))

    a = 5
    b = a
    print(b)

    f = my_func

    print(f(1,2)) # Skriver ut 3. f pekar på samma funktion som my_func
    print(f) # Titta på adressen som skrivs ut. Det är samma som när vi gör print(my_func) f och my_func pekar båda på samma funktion
    print(type(f))

    l1 = [1, 2, 3]
    l2 = l1

    l1.append(4)

    print(l2)
    l2.append(5)
    print(l1)


    f_list = []
    f_list.append(my_func)
    f_list.append(func2)
    print(f_list)

    print(my_func.__name__)
    print(f.__name__) # Både f och my_func pekar på samma funktion. Denna fick namnet my_func när den skapades på rad 3

    for func in f_list:
        print(func.__name__, func(10))
