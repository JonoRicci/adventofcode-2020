"""
Day 01 - Solution 01

Puzzle input as file to read.
"""


def main() -> None:
    """
    Call the functions and display.
    """
    expense_list = import_list()
    print(f"Part 1: {find_sum_two(expense_list)}")
    print(f"Part 2: {find_sum_three(expense_list)}")


def import_list() -> list:
    """
    Read file and return list.

    :return: List of integers
    :rtype: list
    """
    file = open("../puzzle-input", "r")
    string_list = list(file.readlines())
    int_list = [int(i) for i in map(str.strip, string_list)]
    file.close()
    return int_list


def find_sum_two(expenses: list, total=2020) -> int:
    """
    Iterate over the list and subtract from total value.

    :param expenses: List of integers
    :param total: Total value
    :return: Product of two values
    :rtype: int
    """
    for first in expenses:
        second = total - first
        if second in expenses:
            return first * second
    raise ValueError("Not solvable")


def find_sum_three(expenses: list) -> int:
    """
    Attempt every calculation while iterating over list to find third entry.

    :param expenses: List of integers
    :return: Product of three values
    :rtype: int
    """
    while expenses:
        selected = expenses.pop()
        remainder = 2020 - selected
        try:
            return selected * find_sum_two(expenses, total=remainder)
        except ValueError:
            continue


if __name__ == "__main__":
    main()
