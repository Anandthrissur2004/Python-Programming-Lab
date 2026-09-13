students = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Print list using list comprehension
print("\nList of students using list comprehension:")

student_list = [s for s in students]

print(student_list)

# Insert a new student in the list
new_student = input("\nEnter a new student name to add: ")

students.append(new_student)

print("Updated list of students:", students)

# Search for a student in the list
search_student = input("\nEnter a student name to search: ")

if search_student in students:
    print(search_student, "is found.")
else:
    print(search_student, "is not found.")

# Update a student's name in the list
update_student = input("\nEnter a student name to update: ")

if update_student in students:
    new_name = input("Enter the new name: ")

    update_index = students.index(update_student)
    students[update_index] = new_name

    print("Updated list of students:", students)
else:
    print(update_student, "is not found.")

# Filter students whose names have more than 4 characters
filtered_students = [s for s in students if len(s) > 4]

print("\nStudents with more than 4 characters:")
print(filtered_students)

# Manipulate the list - sort students alphabetically
students.sort()

print("\nStudents after sorting:")
print(students)

# Reverse the list
students.reverse()

print("\nStudents after reversing:")
print(students)