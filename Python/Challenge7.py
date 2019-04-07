# Area of a Rectangular Room - Create a program that calculates the area of a room
# Prompt the user for the length and width of the room in feet. Then display the
# area in both square feet and square meters.
# Date: 1-17-19

# Constraints:  Keep the calculations separate from the output
#               Use a constant to hold the conversion factor

# Challenges:   Revise the program to ensure that inputs are entered as numeric
#                   Don't allow the user to proceed if the value entered is not. (1-17-19)
#               Create a new verson that allows you to coose feet or meters for inputs (1-17-19)
#               Implement this as a GUI program that automatically updates values

# Test case
# Input1:   15
# Input2:   20
# Output:   The Area is
#           300 square feet
#           27.871 square meters

import math

FEETTOMETER = 0.09290304

uom = int(input('Feet (0) or meters (1)? '))

def isAnInt(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return False

while True:
    length = isAnInt(input('What is the length of the room? '))
    if length == False:
        print('Please enter a number')
    else:
        break

while True:
    width = isAnInt(input('What is the width of the room? '))
    if width == False:
        print('Please enter a number')
    else:
        break

if uom == 0:
    print(f'You entered dimensions of {length} feet by {width} feet.')
    ftArea = length * width
    mArea = float(ftArea) * FEETTOMETER
    print(f"""The area is\n{ftArea} square feet\n{round(mArea,3)} square meters""")
else:
    print(f'You entered dimensions of {length} feet by {width} meters.')
    mArea = length * width
    ftArea = float(mArea) / FEETTOMETER
    print(f"""The area is\n{ftArea} square feet\n{round(mArea,3)} square meters""")

