import requests


def line(t=""):
    print(f"{t:-^100}")


# Om vi har en lista som följande
list_of_nums = [1, 2, 3, 4, 5, 6]
# och vi vill skapa en ny lista som innehåller kvadraten av varje tal
# Vad vi gjort så här långt är något i stil med
line(" Med for-loop")
res = []
for n in list_of_nums:
    res.append(n * n)

print(res)

# Istället kan vi använda en list comprehension för att direkt skapa en ny lista

line(" Med list comprehension ")
res2 = [n * n for n in list_of_nums]
print(res2)  # Vi får exakt samma resultat som tidigare


def square(i):
    return i * i


line(" List comprehension med funktionsanrop ")
res3 = [square(n) for n in list_of_nums]
print(res3)

# På högersidan av in kan vara något som går att iterera över, inte nödvändigtvis en lista
line(" List comprehension med funktionsanrop över en iterator ")
res4 = [square(n) for n in range(1, 7)]
print(res4)

# Vi kan lägga till ett vilkor för att filtrera fram de värden som skall användas i en list comprehension
# I det här fallet vill vi bara kvadrera de jämna talen i listan list_of_nums
line(" List comprehensions med villkor ")
res5 = [square(n) for n in list_of_nums if n % 2 == 0]
print(res5)

# Motsvarande med en for-loop skulle se ut så här kanske
res6 = []
for n in list_of_nums:
    if n % 2 == 0:
        res6.append(n * n)
print(res6)

# line(" Uppgift 58 ")

# questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()['questions'] print(questions) 1.
# Skriva en list comprehension som skapar en lista med alla prompter från frågorna. 2. Skriva en list comprehension
# som skapar en lista med alla prompter från frågorna där antalet gånger frågan ställts är över 500

# all_prompts = [question['prompt'] for question in questions if int(question['times_asked']) > 500]
# print('\n'.join(all_prompts))


line(" Uppgift 57 ")
# Använd funktionen reduce (som du hittar i modulen functools) för att skapa en funktion som kontrollerar om alla
# värden i en lista är sanna och ger true eller false tillbaks Den kan ha följande signatur all_true(l: list) -> bool
#
#
# Exempel på körning
#
#
# all_true([True, True, True]) -> True
#
#
# all_true([True, False, True, True]) -> False
case1 = [True, True, True]
case2 = [True, False, True, True]

def all_true(l: list) -> bool:
    for v in l:
        if not v:
            return False
    return True

print(all_true(case1))
print(all_true(case2))

from functools import reduce
def both_true(a: bool, b:bool) -> bool:
    return a and b

line(" Med reduce och en namngiven funktion ")
print(reduce(both_true, case1))
print(reduce(both_true, case2))

line(" Med reduce och ett lambda-uttryck ")
print(reduce(lambda a, b: a and b, case1))
print(reduce(lambda a, b: a and b, case2))
# lambda kan vi använda för att skapa en funktion för att använda i exempelvis, map, reduce, filter, sorted etc.

line(" Dictionary comprehensions ")
# Vi vill skapa en dictionary med ett tal som nyckel och kvadraten av talet som värde. Lite som de inledande exemplen på list comprehensions

squares = {}
for n in list_of_nums:
    squares[n] = n*n

print(squares)
print(squares[4])

squares2 = {n: n*n for n in list_of_nums}
print(squares2)
print(squares2[4])

# line(" Uppgift 59 ")
# questions = requests.get("https://bjornkjellgren.se/quiz/v2/questions").json()['questions']
#
# line(" Utand dictionary comprehension ")
#
# all_questions = {}
# for question in questions:
#     q_id = question['id']
#     q_id = int(q_id)
#     all_questions[q_id] = question
# # print(all_questions)
# print(all_questions[11])
#
# all_questions2 = {int(question['id']): question for question in questions}
# print(all_questions2[11])

line(" Lambdauttryck är funktioner ")
min_lambda_func = lambda n: n % 2 == 0 # Kontrollerar om talet n är jämt

print(min_lambda_func(10))
print(min_lambda_func(11))

line(" Uppgift 60.1 ")
#60.1 Skriv om funktionen add_as_def som lambda, och lagra i en variabel

def add_as_def(a, b):
    return a + b

add_as_lambda = lambda a, b: a+b # Ingenting man normalt sett gör i ett normalt program, vill vi ha en funktion med
# ett namn skapar vi den med def

print(add_as_def(5, 2))
print(add_as_lambda(5, 2))

# 60.4 Vad kommer följande program att skriva ut? Läs och diskutera först.
# Testkör därefter, och förklara varför ni får det resultat ni får...

line(" Uppgift 60.4 ")
anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[2])
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")

# 60.5 skriv så att vi sorterar på ålder
