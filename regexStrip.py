# python3
# regexStrip.py — An exercise in replicating the functionality of strip method using regex.

import re


def strip_func(usertext, userpattern):
    try:
        space_regex = re.compile(r'(^\s+)(\w.*\.+)(\s+$)')
        spaces = space_regex.findall(usertext)
        front_spaces = spaces[0][0]
        trimmed_string = spaces[0][1]
        back_spaces = spaces[0][2]
        total = len(front_spaces + trimmed_string + back_spaces)
        print(f"The user input a total of {total} characters.")
        print(f'A total of {len(front_spaces) + len(back_spaces)} spaces were removed.')
        print(f'The resulting string ({trimmed_string}) is {len(trimmed_string)} characters in length.')
    except:
        pattern_detect = re.compile(userpattern)
        print(pattern_detect.sub('', usertext))


user_text = input('Please enter text here: ')
user_pattern = input('For pattern strip function, enter pattern. For space strip function, enter None: ')

strip_func(user_text, user_pattern)
