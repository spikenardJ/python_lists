# Question 1: Python List Transformation

# Task 1: Given the list of grades, Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

# Task 2: Calculate the average grade and display it.

grades_average = sum(grades) / len(grades)
print(grades_average)

# Task 3: Replace any grade below 80 with the value Failed.

grades = ["Failed" if item < 80 else item for item in grades]
print(grades)