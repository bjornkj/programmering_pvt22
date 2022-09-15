# Uppgift 3:

# Kod utan indentering följer. Uppgiften är att rätta till programmet med TAB eller SPACE så att det går att köra igen:
import random

n = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20. Guess which?")
while True:
text = input("Your guess: ")
as_number = int(text)

if as_number == n:
print("Correct!")
break

if as_number < n:
print("Wrong, my number is higher... Try again!")

if as_number > n:
print("Wrong, my number is lower... Try again!")