#python3
#regexStrip.py — An exercise in replicating the functionality of strip method using regex.

import re

def spaceStripper(text):
    frontSpace = re.compile(r'(^\s+)(\w.*\.?)(\s{2,})')
    spaces = frontSpace.findall(text)
    print(spaces)
    print(text)

user_input = input('Please enter spaced out text here: ')
spaceStripper(user_input)
