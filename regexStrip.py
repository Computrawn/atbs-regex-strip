# python3
# regexStrip.py — An exercise in replicating the functionality of strip method using regex.

import re


def strip_func(text, pattern):
    if pattern == ' ':
        space_regex = re.compile(r'(^\s+)(\w.*\.+)(\s+$)')
        spaces = space_regex.findall(text)
        spaces_removed = spaces[0][1]
        print(spaces_removed)
    else:
        pattern_regex = re.compile(pattern)
        pattern_removed = pattern_regex.sub('', text)
        print(pattern_removed)


user_text = input('Please enter text here: ')
user_pattern = input('To remove a pattern, type exactly what you want to remove. To remove spaces, press space bar '
                     'followed by return key: ')

strip_func(user_text, user_pattern)
