# 37.1 Skapa en funktion som läser in namn och ålder på en person och skriver ut en hälsning.
# Ex:
# Namn?> Björn
# Ålder?> 40
# Björn är 40 år gammal!
#
#
# Använd en f-sträng för utskriften

def get_name():
    return input("Namn?>")

def get_age():
    return input("Age?>")


def greet():
    name = get_name()
    age = get_age()

    print(f"{name} är {age} år gammal!")


greet()
