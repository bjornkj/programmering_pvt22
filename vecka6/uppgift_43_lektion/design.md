# TODO-applikation


Uppgifter skall ha en text och en due-date
Skall representeras av en klass Task

Programmet skall ha en lista av uppgifter

Uppgifter skall sparas som json

1. Uppgift 1 due: 2022-11-10
2. Uppgift 2 med lite mer text
3. Uppgiften nummer 3

Ta bort> 1

# Funktioner
- Läsa in uppgifter från en fil
- Skriva uppgifter till en fil
- Lista uppgifter
  - Ta varje uppgift från listan av uppgifter och skriv ut
- Ta bort uppgifter
  - Skriv ut alla uppgifter med en nummer framför och låt användaren välja vilken som skall bort
  - Något sätt att hantera att man inte vill ta bort något
    - Om användaren skriver a istället för en siffra så tar vi inte bort något
- Lägg till en uppgift
    - Prompt ny uppgift> Här skriver man den nya uppgiften
    - due date> 2022-11-01
    - Inget due date skall vara ett ok alternativ
    - Lägg till den nya uppgiften sist i listan av uppgifter.
    - Om användaren inte matar in någonting så avbryter vi
- Något sätt att separera uppgifter från meny vid utskrift