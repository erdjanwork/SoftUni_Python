student_by_course = {}

while True:
    line = input()
    if line == 'end':
        break
    course, name = line.split(' : ')

    if course not in student_by_course:
        student_by_course[course] = []

    student_by_course[course].append(name)


for course_name, students in student_by_course.items():
    print(f"{course_name}: {len(students)}")

    for student in students:
        print(f"-- {student}")