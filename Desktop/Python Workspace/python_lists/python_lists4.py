# Question 4: Deep Dive into Python List

# Task 1: Given the lists: Filter out students who have grades below 80. Print the name, grade and activiy.

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

grades_below_80 = sorted(i for i in grades if i < 80)
print(grades_below_80)
print(grades.index(78))
print(students[2], grades[2], activities[2])

# Task 2: For the remaining students, add students name in a new list named students_approved.

students_approved = list(i for i in students if i != "Jane")

# Task 3: Print the list students_approved

print(students_approved)
