"""
Day 02 - Solution 01

"""

import re


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    password_list = import_list()
    result = find_invalid(password_list)
    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[1]}")


def import_list() -> list:
    """
    Import the puzzle input and return a list.

    :return: List of passwords
    :rtype: list
    """
    file = open("../puzzle-input", "r")
    string_list = file.read().splitlines()
    file.close()
    return string_list


def find_invalid(passwords: list) -> int:
    """
    Iterate through list, parse line, increase count when positive find.

    :return: Two integers
    :rtype: int
    """
    part1 = 0
    part2 = 0

    for password in passwords:
        # Parse the line into tuple groups
        pmin, pmax, pchar, pstring = re.search(
            "([0-9]+)-([0-9]+) (.): (.+)", password
        ).groups()  # .groups() returns each match as tuple

        pmin = int(pmin)
        pmax = int(pmax)

        # Add to counter if values are present
        # Part 1: Count occurances of character
        part1 += pmin <= pstring.count(pchar) <= pmax

        # Add to counter if (string[position] == char)
        # Part 2: Count occurances of positional characters
        part2 += (pstring[pmin - 1] == pchar) ^ (pstring[pmax - 1] == pchar)
        # Set symmetric difference with ^
    return part1, part2


if __name__ == "__main__":
    main()
