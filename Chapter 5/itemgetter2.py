from operator import itemgetter

students =[
    {"name":"jane", "age":12, "grade":'A'},
    {"name":"dave", "age":32, "grade":'B'},
    {"name":"sally", "age":17, "grade":'B'},
]

print(type(students)) # list

results = sorted(students, key=itemgetter('age'))
print(type(results)) # list
print(results)