# Mad Lib - Create a simple mad-pib program that prompts for a noun, a verb,
# an adverb, and an adjective and injects those into a story that you create.
# Date: 1-16-19

# Constraints:    Use a single output statment
#               USe string interpolation or string substitution

noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adj = input('Enter an adjective: ')
adv = input('Enter an adverb: ')
print(f"""Do you {verb} your {adj} {noun} {adv}? That's hilarious!""")