"""
Day 05 - Solution 01

"""


def main() -> None:
    """
    x

    """
    data = import_puzzle()
    print(data)


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
