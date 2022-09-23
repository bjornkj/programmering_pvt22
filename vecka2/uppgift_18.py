people = {
    "Björn": "0445654653",
    "Olof": "123456789",
    "Lisa": "9999999999",
    "Bodil": "555-666-789"
}

vem = input("Vem vill du ringa?")
if vem not in people:
    print("Ledsen, vet inte vem det är")
else:
    number = people[vem]
    print(f"Numret till {vem} är {number}")

# 18.1 Försök beskriva vad programmet gör
# 18.2 Modifiera programmet så antalet personer i telefonkatalogen skrivs ut när man kör programmet
# 18.3 Flytta in all kod i en "main"-funktion som anropas på slutet av programmet.
#   Main ska varken ta argument, eller returnera något
# 18.4 Ge användaren ett val mellan "Slå upp" och "Lägg till/skriv över" nummer.