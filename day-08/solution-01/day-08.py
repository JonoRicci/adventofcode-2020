"""
Day 08 - Solution 01

"""


def main() -> None:
    """
    Imports puzzle input, processes data and displays result.

    """
    all_instructions = import_puzzle()

    # Part 01
    accumulator = get_accumulator(all_instructions)
    print(
        f"Part 01: The accumulator value before any second execution is {accumulator}."
    )

    # Part 02
    # Loop that switches jump to nop, and determine whether it hits repeat or end of file.
    # If it hits repeat, return to loop and switch changed values back.
    # Continue loop and change next value.
    for i in range(len(all_instructions)):
        if "jmp" in all_instructions[i]:
            all_instructions[i] = all_instructions[i].replace("jmp", "nop")
            accumulator, found = get_part02(all_instructions)

            if found:
                print(
                    f"Part 02: The accumulator value before before termination is {accumulator}."
                )
                break  # Don't like this break here
            else:
                all_instructions[i] = all_instructions[i].replace("nop", "jmp")


def get_part02(all_instructions: list) -> tuple[int, bool]:
    """
    Iterate over first-time executions, using if elif to execute instructions.

    :return: Accumulator total and boolean on status
    :rtype: tuple of int and bool
    """
    acc = 0
    line = 0
    instructions = []

    while line not in instructions:
        instructions.append(line)
        current_instruction = all_instructions[line]
        current_instruction = current_instruction.split()

        command = current_instruction[0]
        number = int(current_instruction[1])

        if command == "acc":
            acc += number
            line += 1

        elif command == "jmp":
            line += number

        elif command == "nop":
            line += 1

        if line >= len(all_instructions):
            return acc, True

    return acc, False


def get_accumulator(all_instructions: list) -> int:
    """
    Iterate over first-time executions, using if elif to execute instructions.

    :return: Total accumulated
    :rtype: int
    """
    acc = 0
    line = 0
    instructions = []

    while line not in instructions:
        instructions.append(line)
        # Get current line
        current_instruction = all_instructions[line]
        current_instruction = current_instruction.split()

        # Split command and number from string
        command = current_instruction[0]
        number = int(current_instruction[1])

        # Render instructions
        if command == "acc":
            acc += number
            line += 1

        elif command == "jmp":
            line += number

        elif command == "nop":
            line += 1

    return acc


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
