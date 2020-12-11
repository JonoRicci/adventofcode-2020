"""
Day 09 - Solution 01

"""


def main() -> None:
    """
    Imports puzzle input, processes data and displays result.

    """
    data_stream = import_puzzle()

    # Part 01
    invalid_number = get_invalid_number(data_stream)
    print(f"Part 01: The invalid number is {invalid_number}.")

    # Part 02
    print(
        f"Part 02: The encryption weakness number is {get_encryption_weakness(data_stream, invalid_number)}."
    )


def get_encryption_weakness(data_stream: list, invalid_number: int) -> int:
    """
    Loop through the whole data stream (minus the last value).
    For each number in loop, loop through rest of numbers in stream.
    If the sum of the numbers so far is equal to invalid number then yee haw.

    :return: The sum of the min and max of the contiguous stream.
    :rtype: int
    """
    found = False

    for i in range(len(data_stream) - 1):
        numbers = [data_stream[i]]
        for j in range(i + 1, len(data_stream)):
            numbers.append(data_stream[j])

            if sum(numbers) == invalid_number:
                found = True
                break

            elif sum(numbers) > invalid_number:
                break

        if found:
            break

    return min(numbers) + max(numbers)


def get_invalid_number(data_stream: list) -> int:
    """
    Loop through all to end starting at 26th index.
    First 25 are pre-amble.
    We loop through every combination of j and k in preamble.

    :return: The invalid number
    :rtype: int
    """
    for i in range(25, len(data_stream)):
        preamble = data_stream[i - 25 : i]
        number = data_stream[i]
        found = False

        # Loop through every combination
        for j in range(len(preamble) - 1):
            for k in range(j + 1, len(preamble)):
                if preamble[j] + preamble[k] == number:
                    found = True
                    break  # Inner loop
            if found:
                break  # Outer loop

        if found:
            continue

        return number


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
