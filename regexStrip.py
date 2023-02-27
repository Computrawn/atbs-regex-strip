#python3
#regexStrip.py — An exercise in replicating the functionality of strip method using regex.

import re

def spaceStripper(text):
    regexStrip = re.compile(r'(^\s+)(\w{1,})')
    spaced_out = regexStrip.findall(text)
    print(spaced_out)

user_input = input('Please enter spaced out text here: ')
spaceStripper(user_input)
