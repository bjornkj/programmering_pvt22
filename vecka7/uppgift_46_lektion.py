# 1.
# Byta innehål i variabler

a = 1
b = 2

print(f"a:{a} b:{b}")

b, a = a, b

print(f"a:{a} b:{b}")

# 2. Skriv kod för att hitta minsta värdet i en tuple
# med en forloop


t = (12, 5, 7, 129, 3)
smallest_so_far = t[0]
for n in t:
    if n < smallest_so_far:
        smallest_so_far = n

print(smallest_so_far)

print(min(t))


print(max(t))