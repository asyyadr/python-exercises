students = {}

number = input('student number: ')
name = input('student name: ')
surname = input('student surname: ')
class1 = input('student class: ')

students.update({
    number: {
        'name': name,
        'surname': surname,
        'class': class1
    }
})

number = input('student number: ')
name = input('student name: ')
surname = input('student surname: ')
class1 = input('student class: ')

students.update({
    number: {
        'name': name,
        'surname': surname,
        'class': class1
    }
})

# print(students)

student = input('student number? = ')
stdnt = students[student]
print(stdnt)
