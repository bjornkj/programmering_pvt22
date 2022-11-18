import requests

API_URL = "https://bjornkjellgren.se/quiz/v2/questions"
PROXIES = None

question_num = 0
num_correct = 0
question_user_got_wrong = []

for question in requests.get(API_URL, proxies=PROXIES).json()['questions']:
    question_num += 1
    print(f"({question_num})", question['prompt'])

    for i, a in enumerate(question['answers'], start=1):
        print(f"{i}>", a['answer'])

    while True:
        try:
            user_answer = int(input(">"))
            if 1 <= user_answer <= len(question['answers']):
                break
        except ValueError:
            pass
        print(f"Skriv ett tal mellan 1 och {len(question['answers'])}")

    if question['answers'][user_answer - 1]['correct']:
        print("Rätt!")
        num_correct += 1
    else:
        print("Fel!")
        question_user_got_wrong.append((question, user_answer))
    print("-" * 80)
print("%"*80)
print(f"Du fick {num_correct} av {question_num} rätt!")
print("Följande frågor besvarades fel")
for question, ans in question_user_got_wrong:
    print(question['prompt'])
    print("Du svarade:")
    print(question['answers'][ans - 1]['answer'])
    print("Rätt svar är:")
    for i, a in enumerate(question['answers'], start=1):
        if a['correct']:
            print(f"{i}> {a['answer']}")
    print("-"*80)
