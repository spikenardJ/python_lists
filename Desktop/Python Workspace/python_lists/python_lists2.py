# Question 2: Advanced List Methods and Identity Operators

# Task 1: Given the two lists: Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended_and_submitted = [set(attended) & set(submitted)]

print(attended_and_submitted)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

if sorted(submitted) == sorted(attended):
    print("The lists are the identical. All the student's names are the same!")
else:
    print("The lists are different. Not all of the student's names are the same.")

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

new_attended = [set(attended) - set(submitted)]
print(new_attended)

# Using REMOVE to remove new_attended individually:

attended.remove("Frank")
attended.remove("Eve")
print(attended)