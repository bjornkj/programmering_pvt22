# 1) heltalen fr.o.m. 1 t.o.m. 10 i ökande ordning


# Lösning 1
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# Lösning 2
# num = 1
# while True:
#     print(num)
#     num += 1 # Samma sak som num = num + 1
#     if num == 11:
#         break

# Lösning 3
# num = 0
# while num < 10:
#     num += 1
#     print(num)


# Lösning 4 med for-loop
# list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in list_of_ints:
#     print(num)
# I loopen ovan.
# Vi tar ett tal i taget från listan, med början på 1, första saken i listan först
# och spara det värdet i en variabel kallad num
# Sedan finns num tillgängligt i kodblocket och vi kan exempelvis skriva ut det


# Med hjälp av range behöver vi inte själva skapa en lista av tal
# Lösning 5
# for num in range(1, 11):
#     print(num)


# 2) udda tal fr.o.m. 1 t.o.m. 49 i ökande ordning
# Lösning 1, kontrollera och skriv bara ut udda tal
# for num in range(1, 50):
#     if num % 2 == 1:
#         print(num)
#         # num % 2 ger divisionsrest vid heltalsdivision, ex 5 % 2 ger 1 eftersom 2*2 + 1 = 5

# Lösning 2, be range att bara ge oss udda tal från 1 till 49
# for num in range(1, 50, 2):
#     print(num)


# 3) heltal fr.o.m. 10 t.o.m. 1 i minskande ordning
# Lösning 1 med en whileloop
# num = 10
# while num != 0:
#     print(num)
#     num = num - 1

# Lösning 2 med reversedfunktionen
# for num in reversed(range(1, 11)):
#     print(num)

# Lösning 3 med range och negativt step
# for num in range(10, 0, -1):
#     print(num)


# 4) summan av talen 7 t.o.m 1000
# Lösning 1 med while-loop
# sum_so_far = 0
# num = 7
# while num <= 1000:
#     sum_so_far = sum_so_far + num
#     num += 1
# print(sum_so_far)

# Lösning 2 med for-loop
# sum_so_far = 0
# for num in range(7, 1001):
#     sum_so_far = sum_so_far + num
# print(sum_so_far)

# Lösning 3 med sum-funktionen och range
# print(sum(range(7, 1001)))


# 5) Skriv ut multiplikationstabeller
# Börja med ettans tabell
# 1*1=1
# 1*2=2
# .
# 1*9=9
# Användaren väljer själv
# t = int(input("Tabell?"))
# for i in range(1, 11):
#     print(f"{t} * {i:2} = {t*i:3}")


# Skriv ut tabellerna 1-9
# for t in range(1, 10):
#     for i in range(1, 11):
#         print(f"{t} * {i:2} = {t*i:3}")
