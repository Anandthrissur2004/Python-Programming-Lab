#Program to Student Performance Analysis System
def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def highest_mark(marks):
    return max(marks)

def lowest_mark(marks):
    return min(marks)

def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def sort_students(students):
    return sorted(students, key=lambda student: student['total'], reverse=True)

n = int(input("Enter the number of students: "))

students_list = []

for i in range(n):
    name = input(f"\nEnter the name of student {i + 1}: ")
    marks = []
    for j in range(3):
        mark = int(input(f"Enter the mark for subject {j + 1}: "))
        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = highest_mark(marks)
    lowest = lowest_mark(marks)
    grade = determine_grade(average)

    students_list.append({
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    })

print("\n==============================================================")
print("\n==== Student Performance Analysis ==== ")

sorted_students = sort_students(students_list)

rank = 1
for student in sorted_students:
    print(f"\nRank {rank}: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Total marks: {student['total']}")
    print(f"Average marks: {student['average']}")
    print(f"Highest mark: {student['highest']}")
    print(f"Lowest mark: {student['lowest']}")
    print(f"Grade: {student['grade']}")
    rank += 1

print("\n==============================================================")