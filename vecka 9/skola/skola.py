from datetime import date


class Address:
    street: str
    street_no: str
    zip_code: str
    city: str
    country: str

    def __init__(self, street: str, street_no: str, zip_code: str, city: str, country: str):
        self.street = street
        self.street_no = street_no
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street} {self.street_no}\n{self.zip_code} {self.city}\n{self.country}"

    def __eq__(self, other):
        return self.street == other.street and self.street_no == other.street_no and self.city == other.city and \
               self.zip_code == other.zip_code and self.country == other.country


class Person:
    first_name: str
    last_name: str
    birth_date: date
    address: Address

    def __init__(self, first_name: str, last_name: str, birth_date: date, address: Address = None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address


class Student(Person):
    credits: int

    def __init__(self, first_name: str, last_name: str, birth_date: date, credits: int, address: Address = None):
        super(Student, self).__init__(first_name, last_name, birth_date, address)
        self.credits = credits


class Teacher(Person):
    email: str
    phone_no: str

    def __init__(self, first_name: str, last_name: str, birth_date: date, email: str, phone_no: str, adress: Address = None):
        super(Teacher, self).__init__(first_name, last_name, birth_date, adress)
        self.email = email
        self.phone_no = phone_no


class Course:
    course_id: str
    name: str
    start_date: date
    end_date: date
    students: list[Student]
    teachers: list[Teacher]

    def __init__(self, course_id: str, name: str, start_date: date, end_date: date):
        self.course_id = course_id
        self.name = name
        self. start_date = start_date
        self.end_date = end_date

        self.students = []
        self.teachers = []

    def enrol(self, student: Student):
        self.students.append(student)

    def disenrol(self, student: Student):
        if student in self.students:
            self.students.remove(student)



if __name__ == '__main__':
    kalles_adress = Address("Ankvägen", "13", "12345", "Ankeborg", "Sverige")
    kalle = Person("Kalle", "Anka", date(1940, 4, 12), kalles_adress)


    kajsas_adress = Address("Ankvägen", "13", "12345", "Ankeborg", "Sverige")
    kajsa = Person("Kajsa", "Anka", date(1942, 1, 28), kajsas_adress)

    print(kalle.first_name)
    print(kalle.address)

    print("-"*80)
    print("Kajsa")
    print(kajsa.address)

    print("-"*80)

    print("Är det samma adress? kalle.adress == kajsa.adress")
    print(kalle.address == kajsa.address)

    print(id(kalle.address))
    print(id(kajsa.address))
    print("-" * 80)

    studenten = Student("Björn", "Kjellgren", date(1980, 12, 4), 230)

    print(studenten.first_name)
    print(isinstance(studenten, Student))
    print(isinstance(studenten, Person))

    larare = Teacher("Läraren", "Lärarsson", date(1970, 1, 30), "asdf@askldjf.com", "12345")

    print(isinstance(larare, Person))
    print(isinstance(larare, Teacher))
    print(isinstance(larare, Student))

