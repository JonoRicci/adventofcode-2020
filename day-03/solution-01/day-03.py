"""
Day 03 - Solution 01

"""


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    landscape = import_puzzle()
    solve_puzzle(landscape)


def import_puzzle() -> list:
    """
    Import the puzzle input as a list of lines.

    :return: List of lines of the landscape
    :rtype: list
    """
    file = open("../puzzle-input", "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def print_puzzle(lines) -> None:
    """
    Print out each line.

    """
    for line in lines:
        print(line)


def solve_puzzle(landscape_lines) -> None:
    """
    Track coordinates, examine each line and traverse entire list of lines.
    When the position has been reached and if a tree exists, count it.

    """

    heading = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    tree_count = []

    for headers in heading:
        line_trees = 0
        x_coords = 0
        y_coords = 0

        while y_coords + 1 < len(landscape_lines):
            x_coords = (x_coords + headers[0]) % len(landscape_lines[0])
            y_coords += headers[1]

            if landscape_lines[y_coords][x_coords] == '#':
                line_trees += 1

        tree_count.append(line_trees)
        print(f"On heading {headers} I will encounter {line_trees} trees.")

    return tree_count


if __name__ == "__main__":
    main()
