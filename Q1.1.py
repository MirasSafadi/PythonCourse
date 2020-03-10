def get_grade(student, name_list, grade_list, course_list):
    i = name_list.index(student)
    grade = grade_list[i]
    course = course_list[i]
    return (course, grade)
def get_max_grade(grade, name_list, grade_list, course_list):
    i = grade_list.index(grade)
    name = name_list[i]
    course = course_list[i]
    return (course, name)

names = ['Ana', 'John', 'Denise', 'Katy']
grades = ['B', 'A+', 'A', 'A']
courses = [2.00, 6.0001, 20.002, 9.01]

info = get_grade('Ana', names, grades, courses)
print(info)
print("student with the highest grade")
info = get_max_grade('A+', names, grades, courses)
print(info)
