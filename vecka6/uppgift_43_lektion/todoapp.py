import datetime
from datetime import date

TASK_FILE = 'tasks.json'

MENU = """1. Lista uppgifter
2. Lägg till uppgift
3. Ta bort uppgift
4. Avsluta programmet"""


class Task:
    text: str
    due_date: date | None

    def __init__(self, text: str, due_date: date = None):
        self.text = text
        self.due_date = due_date

    def __str__(self):
        if self.due_date:
            return f"{self.text} due:{self.due_date}"
        else:
            return self.text


def get_new_task() -> Task | None:
    task_text = input("new task>")
    if task_text == "":
        return None
    due_date_text = input("due date YYYY-MM-DD>")
    try:
        due_date = datetime.datetime.strptime(due_date_text, "%Y-%m-%d").date()
    except ValueError:
        due_date = None
    return Task(task_text, due_date)


def print_task_list(task_list: list[Task]):
    for task in task_list:
        print(task)


def read_tasks(task_file) -> list[Task]:
    return []


def save_tasks(task_list: list[Task], task_file):
    pass


def main():
    task_list: list[Task] = read_tasks(TASK_FILE)
    while True:
        print(MENU)
        user_choice = input(">")
        if user_choice == "1":
            print_task_list(task_list)
        elif user_choice == "2":
            new_task = get_new_task()
            if new_task:
                task_list.append(new_task)
        elif user_choice == "3":
            for i, task in enumerate(task_list, start=1):
                print(f"{i} {task}")
            input("remove>")
        elif user_choice == "4":
            save_tasks(task_list, TASK_FILE)
            break


if __name__ == '__main__':
    main()
