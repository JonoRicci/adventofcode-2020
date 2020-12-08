"""
Day 07 - Solution 01

"""


def main() -> None:
    """
    Imports puzzle input, processes data and displays result.

    """
    list_of_bags = import_puzzle()

    # Part 01
    bags = get_num_bags(list_of_bags, "shiny gold")
    print(
        f"Part 01: Total bag colours that contain at least one shiny gold bag is {len(bags)}."
    )

    # Part 02
    count = get_bag_count(list_of_bags, "shiny gold")
    print(
        f"Part 02: Individual bags required inside my single shiny gold bag is {count - 1}."
    )


def get_bag_count(list_of_bags: list, colour: str) -> int:
    """
    Recursive function to loop through list.
    Gather rules on line.
    While there are still rules to be processed, get colour and recursively call function again.
    Append to total.

    :return: Total amount of bags inside colour.
    :rtype: int
    """
    # Figure out the current rule on line.
    rule = ""
    for line in list_of_bags:
        if line[: line.index(" bags")] == colour:
            rule = line
    # If contains no bags, skip.
    if "no" in rule:
        return 1

    # Get the rest of the string.
    rule = rule[rule.index("contain") + 8 :].split()

    # Iterate over bags in rule, recursively searching for each bag.
    total = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        colour = rule[i + 1] + " " + rule[i + 2]
        total += count * get_bag_count(list_of_bags, colour)
        i += 4

    return total + 1


def get_num_bags(list_of_bags: list, colour: str) -> list:
    """
    Recursive function to loop through list.
    Start with shiny gold bag, find bags inside.
    Call itself and search through child bags.
    Search for unique colours in tracking list.

    :return: A list of unique colours.
    :rtype: list
    """
    # Return a list of lines which include the "colour".
    lines = [
        line for line in list_of_bags if colour in line and line.index(colour) != 0
    ]

    all_colours = []
    if len(lines) == 0:
        return []
    else:
        # Return a list of parent colour bags.
        colours = [line[: line.index(" bags")] for line in lines]
        # all_colours tracks colours we have checked.
        # This gathers colours we haven't checked yet.
        colours = [colour for colour in colours if colour not in all_colours]

        # Recursively gather all colours.
        for colour in colours:
            all_colours.append(colour)
            bags = get_num_bags(list_of_bags, colour)
            all_colours += bags

        # Gather unique colours to return.
        unique_colours = []
        for colour in all_colours:
            if colour not in unique_colours:
                unique_colours.append(colour)

        return unique_colours


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
