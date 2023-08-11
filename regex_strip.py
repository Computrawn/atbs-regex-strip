#!/usr/bin/env python3
# regexStrip.py — An exercise in understanding regular expressions.
# For more information, see README.md

import logging
import re

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.

"""This could be better, but regexes are the worst and why reinvent the wheel, man?"""

special_characters = ["*", "$", "+", "^", "()", "(", ")"]


def strip_func(text: str, pattern: str) -> str:
    if not pattern:
        beginning_spaces = re.compile(r"^\s*")
        ending_spaces = re.compile(r"\s*$")
        characters_removed = beginning_spaces.sub("", text)
        characters_removed = ending_spaces.sub("", characters_removed)
    elif pattern in special_characters:
        pattern_regex = re.compile(f"[\{pattern}*]")
        characters_removed = pattern_regex.sub("", text)
    else:
        pattern_regex = re.compile(pattern)
        characters_removed = pattern_regex.sub("", text)
    logging.debug(f"____{text}____ converted to ____{characters_removed}____")
    return characters_removed


def main() -> None:
    text = input("Please enter text here: ")
    pattern = input(
        """Type all characters you want to remove or press enter to remove all spaces.
To remove spaces, press return key: """
    )
    print(strip_func(text, pattern))


if __name__ == "__main__":
    main()
