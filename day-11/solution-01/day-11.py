"""
Day 11 - Solution 01

"""

from typing import Tuple  # Type hinting for multiple returns


def main() -> None:
    """
    Imports puzzle input, processes data and displays result.

    """
    original_seating = import_puzzle()
    final_seating_count = get_final_count(original_seating)
    print(
        f"Part 01: There are {final_seating_count[0]} occupied seats after {final_seating_count[1]} rounds of changes."
    )


def get_final_count(seating: list) -> Tuple[int, int]:
    """
    Take in the original seating layout, and render the seating rules against it.
    Iterate over the new round of seating and apply the rules again.
    Continue to do this until there the previous iteration is identical to the current iteration.

    :return: Total count of occupied seats.
    :rtype: int
    """
    previous = seating.copy()
    render_rules(seating)

    seating_rounds = 0
    while seating != previous:
        previous = seating.copy()
        render_rules(seating)
        seating_rounds += 1

    occupied_seats = get_occupied_seats(previous)

    return occupied_seats, seating_rounds - 1


def render_rules(seating: list) -> list:
    """
    Iterate over every position in the seating area.
    If a seat (empty or occupied) has been found, calculate the seats around it.
    Modify the seat as appropriate.
    Append to a new list of list of the seating arrangement.

    """
    seating_iteration = []
    for row in range(len(seating)):
        current_row = seating[row]
        new_row = []

        for column in range(len(current_row)):
            if current_row[column] == ".":
                new_row.append(".")
                continue

            adjacent_count = get_adjacent_count(seating, row, column)

            if current_row[column] == "L" and adjacent_count == 0:
                new_row.append("#")
            elif current_row[column] == "#" and adjacent_count >= 4:
                new_row.append("L")

            else:
                new_row.append(current_row[column])
        seating_iteration.append(new_row)

    for i in range(len(seating)):
        seating[i] = seating_iteration[i]

    return seating_iteration


def get_adjacent_count(seating: list, row: int, column: int) -> int:
    """
    Take the current iteration of seating layout, and the position.
    Multiple if statements to add to counter when rules are true.

    :return: Count of adjacent occupied seats.
    :rtype: int
    """
    count = 0
    current_row = seating[row]

    # Check West
    if column - 1 >= 0:
        if current_row[column - 1] == "#":
            count += 1

    # Check East
    if column + 1 <= len(current_row) - 1:
        if current_row[column + 1] == "#":
            count += 1

    # Check North
    if row - 1 >= 0:
        north_row = seating[row - 1]
        if north_row[column] == "#":
            count += 1

        if column - 1 >= 0:
            if north_row[column - 1] == "#":
                count += 1

        if column + 1 <= len(north_row) - 1:
            if north_row[column + 1] == "#":
                count += 1

    # Check South
    if row + 1 <= len(seating) - 1:
        south_row = seating[row + 1]
        if south_row[column] == "#":
            count += 1

        if column - 1 >= 0:
            if south_row[column - 1] == "#":
                count += 1

        if column + 1 <= len(south_row) - 1:
            if south_row[column + 1] == "#":
                count += 1

    return count


def get_occupied_seats(seating: list) -> int:
    """
    Iterate over list of lists and for each item check if string is '#' (occupied).

    :return: Count of occupied seats.
    :rtype: list
    """
    count = 0
    for i in range(len(seating)):
        for j in range(len(seating[i])):
            if seating[i][j] == "#":
                count += 1
    return count


def import_puzzle() -> list:
    """
    Import the raw puzzle-input and return.

    :return: File as list of lines
    :rtype: list
    """
    with open("../puzzle-input") as file:
        data = file.readlines()
        data = [list(line.strip()) for line in data]
        return data


if __name__ == "__main__":
    main()
