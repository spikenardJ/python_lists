# Question 3: Advanced Slicing Techniques

# Task 1: Given the list of temperatures: Extract the temperatures for the second week (7 days) of the month.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temperatures = temperatures[7:14]
print(second_week_temperatures)

# Task 2: Extract all the temperatures above 100.

over_hundred_temps = sorted(i for i in temperatures if i > 100)
print (over_hundred_temps)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.reverse()
print(temperatures)
print(temperatures[4:10])