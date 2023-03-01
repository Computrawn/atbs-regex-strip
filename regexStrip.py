# python3
# regexStrip.py — An exercise in replicating the functionality of strip method using regex.

import re


def strip_func(usertext, userpattern):
    if userpattern == ' ':
        space_regex = re.compile(r'(^\s+)(\w.*\.+)(\s+$)')
        spaces = space_regex.findall(usertext)
        spaces_removed = spaces[0][1]
        print(spaces_removed)
    else:
        pattern_regex = re.compile(userpattern)
        pattern_removed = pattern_regex.sub('', usertext)
        print(pattern_removed)


user_text = input('Please enter text here: ')
user_pattern = input('For pattern strip function, enter pattern. For space strip function, press space bar followed '
                     'by return key: ')

strip_func(user_text, user_pattern)
