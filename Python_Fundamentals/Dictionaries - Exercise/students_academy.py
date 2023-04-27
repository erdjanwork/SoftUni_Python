num = int(input())
student_grades = {}

for _ in range(num):
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = []


    student_grades[name].append(grade)

for student,grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade < 4.50:
        continue
    print(f'{student} -> {average_grade:.2f}')

