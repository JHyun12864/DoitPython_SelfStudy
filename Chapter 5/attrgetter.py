from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('jane', 22, 'A'),
    Student('dave', 22, 'B'),
    Student('sally', 17, 'B'),
]

print(type(students)) # list

result = sorted(students, key=attrgetter('age'))
print(type(result)) # list

# for i in result:

