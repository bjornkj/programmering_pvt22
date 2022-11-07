# Uppgift 9:
# 9.1 Fixa så detta program fungerar igen.
# 9.2 Byt till f-string!
# 9.3 Gör så att programmet frågar efter antal uppgifter att lösa
# 9.4 Låt programmet fråga användaren vilket största talet ska vara

import random

def game():
    correct_answers = 0
    for i in range(3):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = input(str(a) + "+" + str(b) + "=")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
        print("---")
        print("Du fick " + str(correct_answers) + " av 3 rätt.")

if __name__ == '__main__':
    game()



