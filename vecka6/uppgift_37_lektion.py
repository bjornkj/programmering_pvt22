# 37.1 Skapa en funktion som läser in namn och ålder på en person och skriver ut en hälsning.
# Ex:
# Namn?> Björn
# Ålder?> 40
# Björn är 40 år gammal!
#
#
# Använd en f-sträng för utskriften


# Skapa en main-funktion i vilken ni:
# 1. Anropar funktionen för att läsa in namn och ålder
# 2. Sparar resultatet i två variabler, name och age
# 3. Anropar funktionen som skriver ut hälsningstexten med name och age som argument.
# 4. Kör main-funktionen från en if __name__ == '__main__' guard'

# 1. Skapa en klass Person som har ett namn och en ålder
# 2. Skriv om funktionen som läser in namn och ålder så att den nu
# returnerar en instans av klassen Person

class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


def get_person() -> Person:
    name = input("Namn?>")
    age = int(input("Ålder?>"))

    return Person(name, age)


def greet(person: Person):
    print(f"{person.name} är {person.age} år gammal!")


def main():
    p = get_person()
    greet(p)


if __name__ == '__main__':
    main()
