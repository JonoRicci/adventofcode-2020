"""
Day 05 - Solution 01

"""


def main() -> None:
    """
    Imports puzzle input, processes data and displays result.

    """
    boarding_passes = import_puzzle()
    list_of_ids = []

    # Part 01
    highest_id = part_01(boarding_passes, list_of_ids)
    print(f"Part 01: The highest seat ID on a boarding pass is {max(highest_id)}")

    # Part 02
    my_seat_id = part_02(list_of_ids)
    print(f"Part 02: Our seat number must be {my_seat_id}")


def part_01(boarding_passes: list, list_of_ids: list) -> list:
    """
    Iterate over all boarding passes, retrieve row and col and seat id.

    :return: List of all seat IDs
    :rtype: list
    """
    for boarding_pass in boarding_passes:
        row = get_row(boarding_pass[:7])  # Get all before 7th
        col = get_col(boarding_pass[7:])  # Get all after 7th
        seat_id = row * 8 + col  # Seat ID calculation
        list_of_ids.append(seat_id)  # Add to total list
    return list_of_ids


def part_02(list_of_ids: list) -> int:
    """
    Iterate over all seat IDs and check conditions to find user's seat.

    :return: User Seat ID
    :rtype: int
    """
    for seat_id in list_of_ids:
        if seat_id + 1 not in list_of_ids and seat_id + 2 in list_of_ids:
            my_seat_id = seat_id + 1
            return my_seat_id


def get_row(boarding_pass: str) -> int:
    """
    For a single boarding pass iterate over each letter.
    Calculate the upper and lower and return.

    :return: The row number
    :rtype: int
    """
    lower = 0
    upper = 127
    for i in range(6):
        half = (upper + lower) // 2
        if boarding_pass[i] == "F":
            upper = half
        elif boarding_pass[i] == "B":
            lower = half + 1
    if boarding_pass[6] == "F":
        return lower
    else:
        return upper


def get_col(boarding_pass: str) -> int:
    """
    For a single boarding pass iterate over each letter.
    Calculate the upper and lower and return.

    :return: The column number
    :rtype: int
    """
    upper = 7
    lower = 0
    for i in range(2):
        half = (upper + lower) // 2
        if boarding_pass[i] == "L":
            upper = half
        elif boarding_pass[i] == "R":
            lower = half + 1
    if boarding_pass[2] == "L":
        return lower
    else:
        return upper


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
