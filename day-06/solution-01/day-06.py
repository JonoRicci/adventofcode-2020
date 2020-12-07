"""
Day 06 - Solution 01

"""


def main() -> None:
    """
    Imports puzzle input, processes data and displays result.

    """
    customs = import_puzzle()

    # Part 01
    response_sum = 0
    current_response = ""
    for line in customs:
        if line != "":
            current_response += line
        else:
            response_sum += get_anyone_answers(current_response)
            current_response = ""

    response_sum += get_anyone_answers(
        current_response
    )  # Once more to get trailing entry
    print(
        f"Part 01: Sum of number of questions anyone answered 'yes' to is {response_sum}"
    )

    # Part 02
    response_sum = 0
    current_response = []
    for line in customs:
        if line != "":
            current_response.append(line)
        else:
            response_sum += get_everyone_answers(current_response)
            current_response = []

    response_sum += get_everyone_answers(
        current_response
    )  # Once more to get trailing entry
    print(
        f"Part 02: Sum of number of questions everyone answered 'yes' to is {response_sum}"
    )


def get_everyone_answers(response: list) -> int:
    """
    Track status with boolean.
    Iterate over input list and each item in list.

    :return: Count of positive answers
    :rtype: int
    """
    in_all_lines = True

    questions = []
    for char in response[0]:
        in_all_lines = True
        for line in response:
            if char not in line:
                in_all_lines = False
        if in_all_lines and char not in questions:
            questions.append(char)
    return len(questions)


def get_anyone_answers(response: str) -> int:
    """
    Iterate over input string and append to list when char
    not in string.

    :return: Count of positive answers
    :rtype: int
    """
    questions = []
    for char in response:
        if char not in questions:
            questions.append(char)
    return len(questions)


def import_puzzle() -> list:
    """
    Import the raw puzzle-input and return.

    :return: File as list of lines
    :rtype: list
    """
    with open("../puzzle-input") as file:
        data = file.readlines()
        data = [line.strip() for line in data]
        return data


if __name__ == "__main__":
    main()
