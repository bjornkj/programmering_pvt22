# Addition av två heltal skrivs ut med hjälp av print-funktionen
print(5 + 5)

# På motsvarande sätt kan vi använda andra räkneoperationer
# -, /, *
# Ex
print(5 - 2)

# Division
print(4 / 2)
# Här får vi resultatet 2.0 och inte 2 som man kanske kunde väntat sig.
# Division kan ge annat än heltal som resultat.
print(5 / 2)

# 2.0 och 2 är inte samma sorts data. 2.0 är exempel på ett flyttal och 2 är ett heltal. Två olika datatyper, sorter av data
# kan se vilken typ ett objekt har genom att använda oss av type()
# Exempel
print(type(
    5))  # Skriv ut den datatyp som 5 hör till <class 'int'> int i det här fallet kommer från engelskans integer d.v.s. heltal

print(type(2.5))  # <class 'float'> float betyder att 2.5 är av typen flyttal
print(type(2 + 3j))  # <class 'complex'> komplexa tal uttrycks som en summa av realdel och imaginärdel.

print(type("hej"))  # <class 'str'> "hej" är en textrsträng, i python typen str
print(type(
    True))  # <class 'bool'> True och False är booleska värden. De används för att uttrycka logiska värden, är någonting sant eller falskt

# Objekt av olika typ är olika sorters saker, de hör till olika kategorier.
# Ex 5 och "5", d.v.s. heltalet 5 är inte samma sak som textsträngen 5
print(5 == "5")  # Här kontrollerar vi huruvida heltalet 5 är lika med strängen "5" och får svaret False
# 3 datatyper är inblandade här
# heltal (int), textsträng(str) "5" och boolska värden (bool)
# heltalet 5 är inte samma sak som texten "5" vilket indikeras av resultatet av jämförelsen, det boolska värdet False eller falskt

print(5 == 5.0)  # Den här jämförelsen fungerar, 5 och 5.0 betraktas som lika trots att de har olika datatyp
# Fler exempel på jämförelser eller andra operationer som ger boolska värden tillbaks?
# >, <, >=, <=, and, or, not

print(5 > 10)  # är 5 större än 10
print(5 < 10)  # är 5 mindre än 10

print(5 < 5)  # är 5 mindre än 5? Nej
print(5 <= 5)  # är 5 mindre än eller lika med 5? Ja
print(5 > 5)  # är 5 större än 5? Nej
print(5 >= 5)  # är 5 större än eller lika med 5? Ja

# Vi kan kombinera olika logiska uttryck med and eller or, och eller
print(
    5 > 10 or 9 == 9)  # Hela uttrycket blir sant om antingen vänstersidan av or eller högersidan eller båda sidor är True
print(5 > 10 and 9 == 0)  # Båda uttrycken måste vara sanna för att helheten med and skall bli sann/True

# not används för att negara logiska uttryck
print(not True)  # inte sant är samma sak som falskt
print(not False)  # inte falskt är samma sak som sant

# Konvertering mellan datatyper
# Vi har använt oss av konvertering mellan sträng och heltal. Användaren har matat in strängen "9" och vi konverterar till heltalet 9
print(type(int("9")))  # <class 'int'>,   int("9") tar textsträngen "9" och konverterar till heltalet 9

print(5 == int(
    "5"))  # Tidigare såg vi att 5 och strängen "5" inte var samma sak. Om vi konverterar strängen till ett heltal fungerar jämförelsen
print(str(5) == "5")  # Vi kan också konverta heltalet 5 till strängen 5
print(float("5.5"))  # Konvertera en sträng till ett flyttal
print(float(5))  # Konvertera ett heltal till ett flyttal

# Vissa operationer som exempelvis addition och multiplikation beter sig olika beroende på datatyperna som används

print(5 + 5)
print("Hej " + "där")

print(5 * 5)
print(5 * "hej")

# Variabler
# Vi använder variabler för att spara ett värde av någon typ för att kunna använda senare i programmet
# En variabel skapas genom att ange ett namn på variabeln och sedan tilldela den ett värde med hjälp av =
# Ex
a = 5  # Skapa en variabel med namnet a, spara värdet 5 i den
print(a)  # ger 5 ut i terminalen, variabeln a har värdet 5 sparat i sig
print(type(a))  # <class 'int'> värdet som är sparat i a är av typen heltal (int)

# Ofta vill vi styra vad som händer i vårt program beroende på någon typ av villkor. Detta uttrycker vi med if-elif-else
# user_input = int(input(">"))

# if user_input == 0:  # Efter if förväntas ett uttryck som ger ett booleskt värde tillbaks.
#     print("Du skrev in talet 0")
# elif user_input < 0:
#     print("Talet du skrev in är mindre än 0")
# else:
#     print("Du skrev nog in något tal större än 0")

# if user_input:  # Ett heltal skiljt från 0 kommer betraktas som sant i det här fallet.
#     print("Något värde skiljt från 0")
# else:
#     print("Användaren skrev in talet 0")


# Vill vi upprepa ett stycke kod många gånger använder vi någon typ av loop, i python while eller for
# En while loop behöver någon typ av logiskt uttryck som talar om hur länge vi skall upprepa vår kod.

i = 0  # Skapa en variabel med namnet i som vi sedan tilldelar värdet 0
while i <= 5:
    print(f"Hej {i}")
    i = i + 1
print("Nu är loopen klar")

# while True:
#     print("Gör något för evigt") # Eller vi stöter på en break statement


# En annan vanlig situation är att vi har en samling av saker och vi vill upprepa ett stycke kod för varje sak i samlingen.
# Innan vi går vidare kollar vi på några samlingar av saker.
# 1. listor
min_lista = [1, 2, 3, "En text", 5.5, False]  # En lista består av 0 eller fler saker inom [] separerade av ,
# i python behöver inte alla saker i listan vara av samma typ
# Varje tingest i listan kallar vi för ett element, en lista består av 0 eller fler element.
print(type(min_lista))  # <class 'list'> Min lista är ett objekt av typen list, en lista
# En lista har en längd, det vill säga hur många element den innehåller, vi kan ta reda på det med funkionen len
print(len(min_lista))

# Tänk for-loopen som, ta en sak i tage ur samlingen och kör den efterföljande koden
print("-" * 80)
for e in min_lista:  # Ta ett element i taget ur listan min_lista, stoppa det elementet in i en variabel som heter e och kör koden som följer
    print(f"I variabeln e finns värdet {e} som har typen {type(e)}")
print("-" * 80)
# En samling kan vara ganska många olika saker, ex bokstäver i en text, en lista med element, ett set, rader i en textfil
# eller någonting som beter sig som en samling av saker
print(range(10))
print(type(range(10)))
for n in range(10):
    print(n)


# Funktioner
# Många gånger har vi kod som förekommer på många olika ställen. Vi vill exempelvis utföra en beräkning
# på flera ställen i vårt program. Istället för att upprepa oss och skriva samma sak flera gånger kan vi
# skapa ett namngivet stycke kod vi kan återanvända.
# En klassisk funktion tar 0 eller flera värden in och ger ett värde ut
# Typexempel på en funktion kan vara addition

def add(a,
        b):  # def talar om att vi skall skapa en ny funktion, add är namnet på funktionen, a och b är arument, den datan vi tar in
    return a + b  # return avslutar funktionen och lämnar tillbaks det värde som står till höger


print(add(99,
          100))  # Här använder vi funktionen, vi säger att vi anropar den. Det gör vi genom att skriva funktionens namn(argument1, argument2, ...)


# Tips
# En bra tumregel är att en funktion bara skall göra en sak.
# Försök hålla funktionens längd så kort som möjligt
# Namnge funktionen på ett sätt som beskriver vad den gör.
# Om ni kan ange vilka datatyper som förväntas som argument och som ges som returvärde
# Exempel


def sub(a: int,
        b: int) -> int:  # Här talar vi om att argumenten a och b skal ha typen int och att funktionen ger en int som returvärde
    return a - b


# En funktion behöver inte lämna något returvärde
# Den behöver heller inte ta några argument
# def do_something():
#     min_var = input(">")
#     for i in range(int(min_var)):
#         print("Hej")
#
#     print("nu är loopen klar")
#     a = int(input("a>"))
#     print(a*min_var)
#
# do_something()
# Den här typen funktioner kan vi kalla för procedur, en sekvens av operationer

# dictionaries, består av par av nycklar och värden, separerade av ,
telefonbok = {"bjorn": 124155,
              "louise": "198417895",
              "en_lista": [1, 2, 4, 5],
              "en annan nyckel": 1234155}
# En nyckel kan bara förekomma 1 gång, ett värde många gånger

# Vi kan slå upp ett värde med hjälp en nyckel [] används för att ange nyckeln
print(telefonbok['bjorn'])

# Vi kan lägga in saker i dictionaryn på liknande sätt
telefonbok['ny_nyckel'] = 999
print(telefonbok)

# Vi kan också uppdatera ett värde sparat med en viss nyckel
telefonbok['bjorn'] = 11111
print(telefonbok)

# Vi kan enkelt kontrollera om en nyckel förekommer i en dictionary
print("ny_nyckel" in telefonbok)

# Vi kan ta bort ett nyckel/värdepar med del
del telefonbok['ny_nyckel']
print("ny_nyckel" in telefonbok) # Nu skall vi få False som svar. Nyckeln skall vara borta
print(telefonbok)

# Läsa data från textfiler
# fh = open('min_text', encoding='utf-8') # Öppna filen. spara en referens till den öppna filen i variabeln fh
# print(fh.read())  # Använd variabeln fh för att läsa från filen.
# fh.close()  # Stäng den öppna filen

with open('min_text', encoding='utf-8') as fh:  #Om vi använder with kommer python automatiskt stänga filen när vi nått slutet på kodblocket.
    for line in fh: # Textfiler kan vi betrakta som en samling av textrader, så vi kan använda en for-loop för att läsa en i taget.
        print(f"{line.strip()} ({len(line.strip())})") # På de flesta textraderna finns ett osynligt nyradstecken sist som vi tar bort med .strip()