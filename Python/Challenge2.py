# Counting the Number of Characters - Create a program that prompts for an input string
# and displays output that shows the input string and the number of characters the string contains.
# Constraints:  Be sure the output contains the original string
#               Use a single output statement to construct the output
#               Use a built-in function of the programming language to determine the length of the string
# Date: 1/16/19

# Challenges:   If the user enters nothing, state that the user must enter something into the program. (1/16/19)
#               Implement this program using a graphical user interface and update the character counter
#                   every time a key is pressed. If your language doesn't have a friendly GUI lib, try
#                   doing this exercise with HTML and JS.

# Test case 1
# Input: Homer
# Output: Homer has 5 characters.

# Test case 2
# Input: Sam Sohn
# Output: Sam Sohn has 8 characters.


while True:
    inString = input('What is the input string? ')
    result = len(inString)
    if result == 0:
        print('You must enter something into the program.')
    else:
        print(inString + ' has ' + str(result) + ' characters.')
        break
