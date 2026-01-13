# Sample Coding Questions 01 Week 01
# Gonzalo Contaldo

# Question 2: Defining an array (list)
array = [1, 4, 7, 9]


#Question 3: Order of Operations (Fully-Bracketed Version)
a, b, c, d = 1, 2, 3, 4

# Given the following line of code, give the Fully-Bracketed Version of: e = a - b ** c // d + a % c
e_fully_bracketed = a - ((b ** c) // d) + (a % c)

# Question 4: Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# Question 5: Common Functions - User Input
age = int(input("Please enter your age: "))
age += 22
print("Now showing the shop items filtered by age: {}".format(age))
