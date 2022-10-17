#
# l = [2, 34, 56]
#
# l.append(5)
# l.remove(2)
# l.append(5)
# l.remove(5)
#
#
# for i in l:
#     print(i**2)
#
# print(l)
#
# print(l[1])
#
# t = (2, 34, 56)
# for i in t:
#     print(i**3)
#
# print("-"*80)
# print(f"Första elementet i tuplen är {t[0]}")
# print(f"Längden av tuplen är {len(t)}")
#
# point = (100, 200)
# resolution = (1920, 1080)
#
# print(resolution)
# print(type(resolution))
# print(tuple([1,2,4]))


# 1. Bygg en funktion som tar en tuppel med två tal som indata, och returnerar dessa i omvänd ordning. T.ex.
#
# t = (5, 6)
# print(swaptuple(t))
#
# .. ska ge följande utskrift:
#
# (6, 5)


def swaptuple(tp):
    return tp[1], tp[0]


t = (5, 6)
print(swaptuple(t))


# 2. Bygg en funktion som tar in en lista ls, och returnerar en tuppel som bygger på listan. T.ex.
def to_tuple(ls):
    return tuple(ls)


print(to_tuple([1, 2, 3]))


# ... ska ge:

# (1, 2, 3)


def foo():
    print("Hello World!")
    print(t)


foo()
