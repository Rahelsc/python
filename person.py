class Person:
    def __init__(self, fname, lname, birthdate, adress, telephone, email):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.adress = adress
        self.telephone = telephone
        self.email = email

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


class Student(Person):
    def __init__(self, fname, lname, birthdate, adress, telephone, email, courses: list, year):
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
    def __init__(self, fname, lname, birthdate, adress, telephone, email, base_salary, seniority):
        super().__init__(fname, lname, birthdate, adress, telephone, email)
        self.base_salary = base_salary
        self.seniority = seniority


class Lecturer(Employee):
    def __init__(self, fname, lname, birthdate, adress, telephone, email, base_salary, seniority
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


student1 = Student('rahel', 'schwartz', '13/6/2020', 'petch tikva', '054-6472701'
                   , 'rahelsc@gmail.com', ['python', 'js'], 2)

student2 = Student('ronen', 'schwartz', '13/6/2020', 'petch tikva', '054-6472701'
                   , 'rahelsc@gmail.com', ['python', 'cSharp'], 2)

lecturer = Lecturer("prof", 'fessor', '5/9/1970', 'ramat hasharon', '08-6880255', 'scwartz123@gmail.com', '8000', 'high'
                    , '200', ['python'])


def check_who_teaches(teacher: Lecturer, s: Student):
    for i in teacher.teaches_courses:
        for j in s.courses:
            if i == j:
                print(f'{teacher.fname} teaches {i}')
                print(f'{s.fname} studies {i}')


check_who_teaches(lecturer, student1)
