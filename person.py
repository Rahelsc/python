from builtins import property
from datetime import datetime, date


class Person:
    def __init__(self, fname, lname, birthdate: str, adress, telephone, email):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.adress = adress
        self.telephone = telephone
        self.email = email
        today = date.today()
        self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month,
                                                                                   self.birthdate.day))

    def __str__(self):
        return f'שמי הפרטי הוא:{self.fname}' \
               f'-----' \
               f' שם משפחתי הוא: {self.lname}' \
               f'-----' \
               f' אני גרה ב{self.adress}'

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def birthdate(self):
        return self.__birthdate

    # noinspection PyAttributeOutsideInit
    @birthdate.setter
    def birthdate(self, birthdate):
        try:
            year, month, day = map(int, birthdate.split(','))
            self.__birthdate = datetime(year, month, day)
            return self.__birthdate
        except ValueError:
            print("פורמט לא תואם, נסה שוב")

    def calculate_age(self):
        today = date.today()
        self.age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month,
                                                                                   self.birthdate.day))
        return self.age


class Student(Person):
    def __init__(self, fname, lname, birthdate: str, adress, telephone, email, courses: list, year):
        super().__init__(fname, lname, birthdate, adress, telephone, email)
        self.courses = courses
        self.year = year

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses):
        self.__courses = courses


class Employee(Person):
    def __init__(self, fname, lname, birthdate: str, adress, telephone, email, base_salary, seniority):
        super().__init__(fname, lname, birthdate, adress, telephone, email)
        self.base_salary = base_salary
        self.seniority = seniority


class Lecturer(Employee):
    def __init__(self, fname, lname, birthdate: str, adress, telephone, email, base_salary, seniority
                 , hourly_rate, teaches_courses: list):
        super().__init__(fname, lname, birthdate, adress, telephone, email, base_salary, seniority)
        self.hourly_rate = hourly_rate
        self.teaches_courses = teaches_courses

    @property
    def teaches_courses(self):
        return self.__teaches_courses

    @teaches_courses.setter
    def teaches_courses(self, teaches_courses):
        self.__teaches_courses = teaches_courses


student1 = Student('rahel', 'schwartz', '1988,6,13', 'petch tikva', '054-6472701'
                   , 'rahelsc@gmail.com', ['python', 'js'], 2)

student2 = Student('ronen', 'schwartz', '1988,6,13', 'petch tikva', '054-6472701'
                   , 'rahelsc@gmail.com', ['python', 'cSharp'], 2)

lecturer1 = Lecturer("prof", 'fessor', '1970,7,5', 'ramat hasharon', '08-6880255', 'scwartz123@gmail.com', '8000',
                     'high'
                     , '200', ['python'])


def check_who_teaches(teacher: Lecturer, s: Student):
    try:
        for i in teacher.teaches_courses:
            for j in s.courses:
                if i == j:
                    print(f'{teacher.fname} teaches {i}')
                    print(f'{s.fname} studies {i}')
    except TypeError:
        print("only recieves a lecturer and a student, please try again")
    except:
        print("bad input, try again")


check_who_teaches(lecturer1, student1)

print(student1.age)
