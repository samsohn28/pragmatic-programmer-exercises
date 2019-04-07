# Retirement Calculator - Create a program that determines how many years you have left
# until retirements and what year you can retire. It should prompt you for your
# current age and the age you want to retire.
# Date: 1-17-19

# Constraints:  Convert the input to numerical
#               Don't hard code the current year

# Challenge: Handle situations where the program returns a negative number by stating that
#               the user can already retire (1-17-19)

import datetime

age = int(input('What is your current age? '))
ret = int(input('At what age would you like to retire? '))
currentDateTime = datetime.datetime.now()
yearRet = ret - age

if yearRet < 0:
    print('You can already retire!')
else:
    print(f"""You have {yearRet} years left until you can retire.\nIt's {currentDateTime.year}, so you can retire in {currentDateTime.year + yearRet}.""")
