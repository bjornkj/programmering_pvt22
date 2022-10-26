
l = [1, 2, 3, 4, 5]

print(l)
print(type(l))

def foo():
    print("Hello World!")


# Vi kan lägga in vilka objekt som helst i listan. T.ex en funktion som nedan
l2 = [1, 2, 3, "Hej", [5, 6, 7], foo]

print(l2)

# Vi kan hämta ett element ur listan baserat på position
# positionerna börjar räkna från 0, första elementets position är 0

print(l2[0]) # Första saken i listan
print(l2[3]) # Fjärde saken i listan

print(l2[4]) # På femte positionen i listan finns en annan lista
print(l2[4][1]) # l2[4] tar fram det femte elementet ur listan
# Detta är en lista i sig så vi kan använda ett index igen för att hämta
# i det här fallet det andra elementet [1]

# Den sista saken i listan, funktionen foo, ligger på position 6, det vill säga index 5
print(l2[5])
# Vi kan alltid se hur lång en lista är, det vill säga hur många element som
# finns i listan med hjälp av len()
print(len(l2))
print(l2[len(l2)-1]) # len(l2) - 1 för att få indexet till det sista elementet.
# len(l2) ger 6 om det finns 6 element i listan. Sista elementet har index 5

print(l2[-1]) # index -1 ger det sista elementet i listan
print(l2[-3])

# print(l2[-7]) # Det här ger ett fel, vi kan som mest räkna "ett var tillbaks"

# Det här sättet att arbeta med index fungerar även på strängar och tuples
s = "Hello World!"
print(s[0])
print(s[-1])
print(len(s))


l2[-1]()  # Sista elementet var en funktion, vi får vi tag på en referens till den
# kan vi anropa den precis som vilken annan funktion som helst.

s2 = "En lite längre textsträng"
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# [start: stop] genom att ange en start och slutposition kan vi få tag på en del av listan (eller stränge)
# Exempel
print(l3[0:5])  # Fem första elementen i listan med tal
print(s2[0:5])  # De fem första tecknen i strängen s2
# Om start är 0 kan vi utelämna det:
print(l3[:5])
print(s2[:5])

print(s2[1:5])  # Tar fram texten som börjar på index 1 fram till men inte inkluderat index 5

print(s2[:-1])  # Ta fram substrängen fram till men inte inkluderat sista tecknet (som har index -1)

print(s2[4:-2])

l4 = l3[:]  # Om vi inte anger några index så tolkas det som alla element
print(l4)  # l4 är en kopia av l3


# l3[start: stop: step]

print(l3[::2])  # En kopia av listan l3 där vi tar vartannat element med början på det första
print(l3[1::2])  # En kopia av listan l3 där vi tar vartannat element med början på det andra

print(l3[::-1])
print(s2[::-1])
