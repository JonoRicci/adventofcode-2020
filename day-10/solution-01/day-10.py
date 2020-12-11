"""
Day 10 - Solution 01

"""

CHECKED = {}


def main() -> None:
    """
    Imports puzzle input, processes data and displays result.

    """
    adapters = import_puzzle()

    # Part 01
    print(f"Part 01: The product of 1 and 3 differences is {part01(adapters)}.")

    # Part 02
    adapters.append(max(adapters) + 3)
    adapters = sorted(adapters)
    print(
        f"Part 02: The total number of distinct ways you can arrange the adaptors is {part02(adapters, 0)}."
    )


def part01(adapters: list) -> int:
    """
    x

    """
    one_jumps = 0
    three_jumps = 0

    highest = max(adapters)
    adapters.append(highest + 3)
    adapters.append(0)  # Need to include the jump from 0 to 1
    adapters = sorted(adapters)

    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            one_jumps += 1
        else:
            three_jumps += 1

    print(
        f"The highest value is {highest} therefore we can support up to {highest + 3}."
    )
    print(f"There were {one_jumps} one jumps and {three_jumps} three jumps.")
    return one_jumps * three_jumps


def part02(adapters: list, position: int) -> int:
    """
    x

    """
    if position == len(adapters) - 1:
        return 1  #

    if position in CHECKED:
        return CHECKED[position]

    total = 0
    for i in range(position + 1, len(adapters)):
        if adapters[i] - adapters[position] <= 3:
            total += part02(adapters, i)

    CHECKED[position] = total
    return total


def import_puzzle() -> list:
    """
    Import the raw puzzle-input and return.

    :return: File as list of lines
    :rtype: list
    """
    with open("../puzzle-input") as file:
        data = file.readlines()
        data = [int(line.strip()) for line in data]  # Input is list of ints
        return data


if __name__ == "__main__":
    main()
