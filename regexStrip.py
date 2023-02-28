#python3
#regexStrip.py — An exercise in replicating the functionality of strip method using regex.

import re

def spaceStripper(text):
    extraSpace = re.compile(r'(^\s+)(\w.*\.+)(\s+$)')
    spaces = extraSpace.findall(text)
    front_spaces = spaces[0][0]
    trimmed_string = spaces[0][1]
    back_spaces = spaces[0][2]
    total = len(front_spaces + trimmed_string + back_spaces)
    print(f"The user input a total of {total} characters.")
    print(f'A total of {len(front_spaces) + len(back_spaces)} spaces were removed.')
    print(f'The resulting string ({trimmed_string}) is {len(trimmed_string)} characters in length.')

user_input = input('Please enter spaced out text here: ')
spaceStripper(user_input)
