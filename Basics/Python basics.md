#----------------PYTHON-----------------------------------------------

#1. Python is an interpreted, object-oriented, high-level programming language with dynamic semantics
#2. No type declarations of variables, parameters, functions
#3. Makes the Code short and flexible, therefore reduce the cost of program maintenance
#4. Checks the type of code at runtime
#5. Python is case-sensitive

#-----------------INPUT IN PYTHON-------------------------------------
## Exercise: Understanding inputs() ##
name = input('What is your name? ')
color = input('Which colour do you like? ')
print(name + ' likes ' + color)

#-----------------TYPE CONVERSION-------------------------------------
## Exercises: Ask user their weights (in pounds) convert it into kilogram
weight_lbs = input('What is your weight in pounds? ')
weight_kg = 0.45 * float(weight_lbs)
print(weight_kg)

#-----------------STRING CHARACTER COUNT-------------------------------
course = 'Python is "good"'
learn = "'Wilfred'"
print(course[1:-1])

#-----------------FORMATTED STRING-------------------------------------
msg = f'{course} to learn {learn}'
print(msg)

#----------------STRING FUNCTIONS--------------------------------------
course_string = 'Learning Python'
print(len(course_string))
print(course_string.upper())
print(course_string.lower())
print(course_string.title())
print(course_string.find('P'))
print(course_string.replace('Learning','Teaching'))

#---------------IN operator---------------------------------------------
print('Po' in course_string)






