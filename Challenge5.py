# Simple Math - Write a program that prompts for two numbers. Print the sum, difference,
# product, and quotient of those numbers.
# Date: 1/16/19

# Constraints:  Values coming from the users will be strings. Ensure that you convert before doing the math
#               Keep the inputs and outputs separate from the numberical conversaions and processing
#               Generate a single output statement with line breaks in the appropriate spots
# Date:

# Challenges:   Revise the programs to ensure that inputs are enterd as numeric values. Don't allow the user
#                   to proceed if the value is not numeric (1-17-19)
#               Don't allow negative numbers (1-17-19)
#               Break the program into functions that do the conputations (1-17-19)
#               Implement as a GUI program that automatically updates values when any value changes

# Test case 1
# Input:    10
# Input:    5
# Output:   10 + 5 = 15
# Output:   10 - 5 = 5
# Output:   10 * 5 = 50
# Output:   10 / 5 = 2

# Test case 2
# Input:    15
# Input:    5
# Output:   15 + 5 = 20
# Output:   15 - 5 = 10
# Output:   15 * 5 = 75
# Output:   15 / 5 = 3

def isAnInt(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return False

def addi(a,b):
    return a + b

def subt(a,b):
    return a - b

def multi(a,b):
    return a * b

def divi(a,b):
    return a / b


while True:
    num1 = isAnInt(input('What is the first number? '))
    if num1 == False:
        print('Please enter a number.')
    elif num1 < 0:
        print('Please enter a positive number.')
    else:
        break

while True:
    num2 = isAnInt(input('What is the second number? '))
    if num2 == False:
        print('Please enter a number.')
    elif num2 < 0:
        print('Please enter a positive number.')
    else:
        break

add = addi(num1,num2)
sub = subt(num1,num2)
mult = multi(num1,num2)
div = divi(num1,num2)

print(f'{num1} + {num2} = {add}\n{num1} - {num2} = {sub}\n{num1} * {num2} = {mult}\n{num1} / {num2} = {div}')