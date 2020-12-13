"""
Day 11 - Solution 01

"""

from typing import Tuple  # Type hinting for multiple returns


def main() -> None:
    """
    Imports puzzle input, processes seating and displays result.

    """
    original_seating = import_puzzle()

    # Part 01
    seating_count_01 = get_final_count(original_seating, 4)
    print(
        f"Part 01: There are {seating_count_01[0]} occupied seats after {seating_count_01[1]} rounds of changes."
    )

    # Part 02
    seating_count_02 = get_final_count(original_seating, 5)
    print(
        f"Part 02: There are {seating_count_02[0]} occupied seats after {seating_count_02[1]} rounds of changes."
    )


def get_final_count(seating: list, tolerance: int) -> Tuple[int, int]:
    """
    Take in the original seating layout, and render the seating rules against it.
    Iterate over the new round of seating and apply the rules again.
    Continue to do this until there the previous iteration is identical to the current iteration.

    :return: Total count of occupied seats.
    :rtype: int
    """
    previous = seating.copy()
    render_rules(seating, tolerance)

    seating_rounds = 0
    while seating != previous:
        previous = seating.copy()
        render_rules(seating, tolerance)
        seating_rounds += 1

    occupied_seats = get_occupied_seats(previous)

    return occupied_seats, seating_rounds - 1


def render_rules(seating: list, tolerance: int) -> list:
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

            adjacent_count = 0
            if tolerance == 4:
                adjacent_count = get_adjacent_count(seating, row, column)
            elif tolerance == 5:
                adjacent_count = get_updated_adjacent_count(seating, row, column)

            if current_row[column] == "L" and adjacent_count == 0:
                new_row.append("#")
            elif current_row[column] == "#" and adjacent_count >= tolerance:
                new_row.append("L")

            else:
                new_row.append(current_row[column])
        seating_iteration.append(new_row)

    for i in range(len(seating)):
        seating[i] = seating_iteration[i]

    return seating_iteration


def get_updated_adjacent_count(seating: list, row: int, column: int) -> int:
    """
    Take the current iteration of seating layout, and the position.
    Multiple if statements to add to counter when rules are true.

    :return: Count of adjacent occupied seats.
    :rtype: int
    """
    count = 0
    north_seat = row - 1
    south_seat = row + 1
    east_seat = column + 1
    west_seat = column - 1
    n, s, e, w, ne, se, nw, sw = False, False, False, False, False, False, False, False

    while not (n and s and w and e and ne and se and nw and sw):
        # North
        if not n and north_seat >= 0:
            if seating[north_seat][column] == "#":
                count += 1
                n = True
            elif seating[north_seat][column] == "L":
                n = True
        else:
            n = True

        # South
        if not s and south_seat <= len(seating) - 1:
            if seating[south_seat][column] == "#":
                count += 1
                s = True
            elif seating[south_seat][column] == "L":
                s = True
        else:
            s = True

        # East
        if not e and east_seat <= len(seating[row]) - 1:
            if seating[row][east_seat] == "#":
                count += 1
                e = True
            elif seating[row][east_seat] == "L":
                e = True
        else:
            e = True

        # West
        if not w and west_seat >= 0:
            if seating[row][west_seat] == "#":
                count += 1
                w = True
            elif seating[row][west_seat] == "L":
                w = True
        else:
            w = True

        # North West
        if not nw and north_seat >= 0 and west_seat >= 0:
            if seating[north_seat][west_seat] == "#":
                count += 1
                nw = True
            elif seating[north_seat][west_seat] == "L":
                nw = True
        else:
            nw = True

        # South West
        if not sw and south_seat <= len(seating) - 1 and west_seat >= 0:
            if seating[south_seat][west_seat] == "#":
                count += 1
                sw = True
            elif seating[south_seat][west_seat] == "L":
                sw = True
        else:
            sw = True

        # North East
        if not ne and north_seat >= 0 and east_seat <= len(seating[row]) - 1:
            if seating[north_seat][east_seat] == "#":
                count += 1
                ne = True
            elif seating[north_seat][east_seat] == "L":
                ne = True
        else:
            ne = True

        # South East
        if (
            not se
            and south_seat <= len(seating) - 1
            and east_seat <= len(seating[row]) - 1
        ):
            if seating[south_seat][east_seat] == "#":
                count += 1
                se = True
            elif seating[south_seat][east_seat] == "L":
                se = True
        else:
            se = True

        north_seat -= 1
        south_seat += 1
        east_seat += 1
        west_seat -= 1

    return count


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
        seating = file.readlines()
        seating = [list(line.strip()) for line in seating]
        return seating


if __name__ == "__main__":
    main()
