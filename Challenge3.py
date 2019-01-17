# Printing Quotes - Create a program that prompts for a quote and an author. Display
# the quotation and author. Display as: <author> says, "<quote>"
# Date: 1-16-19

# Constraints:    Use a single output statement to produce this output
#               If your language supports string interpolation or substitution, don't
#                   use it for this exercise. Use string concat instead.

# Test case 1
# Input: These aren't the droids you're looking for.
# Input: Obi-wan Kenobi
# Output: Obi-wan Kenobi says, "These aren't the droids you're looking for."

quote = input('What is the quote? ')
author = input('Who is the author? ')
print(author + ' says, "' + quote + '"')