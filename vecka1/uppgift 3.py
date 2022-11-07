# Uppgift 3:

# Kod utan indentering följer. Uppgiften är att rätta till programmet med TAB eller SPACE så att det går att köra igen:
import random

n = random.randint(1, 20)
print("Jag tänker på ett tal mellan 1 och 20")
while True:
    text = input("Din gissning: ")
    as_number = int(text)

    if as_number == n:
        print("Rätt!")
        break

    if as_number < n:
        print("Fel. Talet är högre, försök igen!")

    if as_number > n:
        print("Fel. Talet är lägre, försök igen!")