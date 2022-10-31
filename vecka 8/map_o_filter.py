list_of_nums = list(range(1000)) # 0-999


def even(n: int) -> bool: # Funktionen skall ge True om n är jämt, annars False
    return n % 2 == 0


def odd(n: int) -> bool: # Funktionen skall ge True om talet n är udda, annars False
    return not even(n)


def square(n: int) -> int:
    return n*n

# Här skriver vi ut alla udda tal i listan
# for num in list_of_nums:
#     if num % 2:
#         print(num)


# Alla udda tal med hjälp av filter
# for element in filter(odd, list_of_nums):
#     print(element)
#
# for element in filter(even, list_of_nums):
#     print(element)


# print(list(filter(odd, list_of_nums))) # filter ger en iterator tillbaks. vi skapar en lista från den

# print(list(map(square, [1, 2, 3, 4, 5])))

# Hitta kvadraten av alla udda tal mindre än 100
for n in map(square, filter(odd, range(1, 100))):
    print(n)
