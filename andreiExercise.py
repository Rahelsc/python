import datetime

name = input('What is your name? ')
relationshipStatus = input('what is your relationship status? ')
birth_year = int(input('what year were you born? '))

age = datetime.datetime.now()
realAge = datetime.datetime.now()
age = age.year - birth_year

print(f"""
Hi {name},
I learned you're {relationshipStatus},
and that you're {age} years old.
cool!
""")



