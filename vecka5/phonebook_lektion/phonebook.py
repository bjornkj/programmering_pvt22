# phonebook = [["Björn", "123456", "bjorn.kjellgren@kyh.se"],
#              ["Louise", "1231451", "en@mailadress.com"]]


# En kontakt skulle kunna se ut så här. De olika delarna i en lista.
# namn, telefon, epost i den ordningen
# kontakt1 = ["Björn", "123456", "bjorn.kjellgren@kyh.se"]
# # Vill vi ha telefonnummer kan vi göra
# telefon1 = kontakt1[1]
# namn, telefon, epost = kontakt1
# print(namn)
# print(telefon)
# print(epost)
# Detta är lite otydligt. Vi måste komma ihåg att första elementet är namn etc.


# Lite mer struktur får vi om vi använder en dict
# Nu kan vi få tag på kontaktens olika komponenter med namnet på komponenten
# kontakt2 = {"name": "Björn", "phone": "123124", "email": "bjorn.kjellgren@kyh.se"}
# # ex. epost
# print(kontakt2['email'])


MAIN_PROMPT = """1. Skapa ny kontakt
2. Sök efter namn
3. Ta bort kontakt
4. Skriv ut alla kontakter
5. Avsluta"""


class Contact:
    name: str
    phone: str
    email: str

    def __init__(self, n: str, p: str, e: str):
        self.name = n
        self.phone = p
        self.email = e

    def print_contact(self):
        print(f"name: {self.name}, phone: {self.phone}, email: {self.email}")

    def __str__(self):
        return f"name: {self.name}, phone: {self.phone}, email: {self.email}"


class PhoneBook:
    contacts: list[Contact]

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def delete_contact(self, contact: Contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

    def print_contacts(self):
        for n, contact in enumerate(self.contacts, start=1):
            print(f"{n} {str(contact)}")

    def find_contact(self, name: str) -> list[Contact]:
        res = []
        for contact in self.contacts:
            if contact.name == name:
                res.append(contact)
        return res


def get_new_contact() -> Contact:
    name = input("name>")
    phone = input("phone>")
    email = input("email>")

    return Contact(name, phone, email)


def main():
    phonebook = PhoneBook()
    phonebook.add_contact(Contact("Björn", "123456", "bjorn.kjellgren@kyh.se"))
    phonebook.add_contact(Contact("Louise", "534534", "en@mailadress.se"))
    phonebook.add_contact(Contact("Carl", "N/A", "N/A"))
    while True:
        print(MAIN_PROMPT)
        command = input(">")
        if command == "1":
            new_contact = get_new_contact()
            phonebook.add_contact(new_contact)
        if command == "2":
            name = input("name>")
            found_contacts = phonebook.find_contact(name)
            for contact in found_contacts:
                print(contact)

        if command == "4":
            print("-"*80)
            phonebook.print_contacts()
            print("-" * 80)

        if command == "5":
            break




if __name__ == '__main__':
    main()