import requests as requests


# Vi skall bygga ett quiz-spel
# Vi skall läsa frågor från ett API "https://bjornkjellgren.se/quiz/v2/questions"
# Varje fråga har en lista av svar
# Vi skall ställa frågorna till användaren
# Användaren skall svara på frågor
# Rätt eller fel svar skall skickas tillbaks till APIet
# När alla frågor besvarats skall vi skriva ut totala poängen


# Quiz-spel, API, Användare, Frågor, Svar, Poäng

# Quiz-spel
# Hämtar frågor från API
# Ställer frågor till användaren
# Räknar poäng


# API, hämtar frågor från någon web-tjänst. Skicka data tillbaks till web-tjänsten

# Fråga
# Har, frågeprompt, lista med svar, id, antal gånger frågan ställts, antal gånger som den besvarats korrekt

# Svar
# Har en svarstext, bool som säger om det är rätt eller fel svar

# Spelare
# Kan få frågor
# Kan ge en siffra som svar

class Answer:
    answer_text: str
    correct: bool

    def __init__(self, answer_text: str, correct: bool):
        self.answer_text = answer_text
        self.correct = correct


class Question:
    answers: list[Answer]
    prompt: str
    question_id: int
    times_asked: int
    times_correct: int

    def __init__(self, question_id: int, prompt: str, times_asked: int, times_correct: int, answers: list[Answer]):
        self.question_id = question_id
        self.prompt = prompt
        self.times_asked = times_asked
        self.times_correct = times_correct
        self.answers = answers


class QuizAPI:
    def get_questions(self):
        raise NotImplementedError

    def send_feedback(self, question: Question, answer: Answer):
        raise NotImplementedError


class WebQuizAPI(QuizAPI):
    url: str

    def __init__(self, url):
        self.url = url

    def get_questions(self) -> list[Question]:
        # return [Question(1, "Vilken funktion använder vi för att skriva ut saker i terminalen?", 10, 5,
        #                 [Answer("print()", True), Answer("input()", False)])]
        questions = requests.get(self.url).json()['questions']
        return [self._parse_question(question) for question in questions]

    def send_feedback(self, question: Question, answer: Answer):
        pass

    def _parse_question(self, question) -> Question:
        return Question(int(question['id']), question['prompt'], int(question['times_asked']),
                        int(question['times_correct']),
                        self._parse_answers(question['answers']))

    def _parse_answers(self, answers) -> list[Answer]:
        return [self._parse_answer(ans) for ans in answers]

    @staticmethod
    def _parse_answer(ans) -> Answer:
        return Answer(ans['answer'], bool(ans['correct']))


class BjornsFakeAPI(QuizAPI):
    def get_questions(self) -> list[Question]:
        q1 = Question(1, "Vilken funktion använder vi för att skriva ut saker i terminalen?", 10, 5,
                      [Answer("print()", True), Answer("input()", False)])
        q2 = Question(2, "Vad är meningen med livet universum och allting?", 12, 5,
                      [Answer("Ingen aning", False), Answer("42", True), Answer("50", False)])
        return [q1, q2]

    def send_feedback(self, question: Question, correct: bool):
        pass


class Player:
    def ask_question(self, question: Question) -> Answer:
        raise NotImplementedError


class ConsolePlayer(Player):
    def ask_question(self, question: Question) -> Answer:
        print(question.prompt)
        for i, answer in enumerate(question.answers, start=1):
            print(f"{i} {answer.answer_text}")
        return question.answers[0]


class CheatingPlayer(Player):
    def ask_question(self, question: Question) -> Answer:
        print(question.prompt)
        for i, answer in enumerate(question.answers, start=1):
            print(f"{i} {answer.answer_text}")
        for ans in question.answers:
            if ans.correct:
                return ans


class DunningKrugerPlayer(Player):
    def ask_question(self, question: Question) -> Answer:
        print(question.prompt)
        for i, answer in enumerate(question.answers, start=1):
            print(f"{i} {answer.answer_text}")
        for ans in question.answers:
            if not ans.correct:
                return ans


class Quiz:
    quiz_api: QuizAPI
    player: Player
    questions_asked: int
    questions_correct: int
    failed_questions = list[tuple[Question, Answer]]

    def __init__(self, quiz_api: QuizAPI, player: Player):
        self.quiz_api = quiz_api
        self.player = player
        self.questions_asked = 0
        self.questions_correct = 0
        self.failed_questions = []

    def run(self):
        for question in self.quiz_api.get_questions():
            ans = self.player.ask_question(question)
            self.questions_asked += 1
            if ans.correct:
                self.questions_correct += 1
            else:
                self.failed_questions.append((question, ans))
            self.quiz_api.send_feedback(question, ans)

        self.print_results()

    def print_results(self):

        print(f"{self.questions_correct} of {self.questions_asked} correct")

        print("Du fick fel på följande frågor")
        for question, answer in self.failed_questions:
            print(question.prompt)
            print(f"Du svarade {answer.answer_text}")
            print("Rätt svar är")
            for i, ans in enumerate(question.answers, start=1):
                if ans.correct:
                    print(f"{i}> {ans.answer_text}")


if __name__ == '__main__':
    # q_api = BjornsFakeAPI()
    q_api = WebQuizAPI("https://bjornkjellgren.se/quiz/v2/questions")
    # p = Player()
    # p = CheatingPlayer()
    p = DunningKrugerPlayer()
    quiz = Quiz(q_api, p)
    quiz.run()
