"""
Day 04 - Solution 01

"""

# Global variables
FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
VALID_PASSPORTS = []


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    passports = import_puzzle()

    valid_count = 0
    current_passport = ""

    for line in passports:  # Iterate over the puzzle input
        if line != "":  # If line is not blank (part of passport)
            current_passport += " " + line
        else:  # If line is blank we have reached end of passport
            if part_01(current_passport):
                VALID_PASSPORTS.append(current_passport)
                valid_count += 1
            current_passport = ""  # Reset current_passport

    if part_01(current_passport):
        # Above for loop misses out last password so check here
        VALID_PASSPORTS.append(current_passport)
        valid_count += 1

    print(f"Part 01: There are {valid_count} valid passports.")

    # For part 02 we only examine the valid passports so far from VALID_PASSPORTS.
    valid_count = 0  # Reset valid count
    for passport in VALID_PASSPORTS:
        if part_02(passport):
            valid_count += 1

    print(f"Part 02: There are {valid_count} valid passports.")


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


def part_01(passport: str) -> bool:
    """
    Iterate over input list and check global variable fields are present.

    :return: Status of individual passport (true = valid).
    :rtype: bool
    """
    for field in FIELDS:
        if field not in passport:
            return False
    return True


def part_02(passport: str) -> bool:
    """
    Parse list into dictionary and validate each field.

    :return: Status of individual passport (true = valid).
    :rtype: bool
    """
    passport = passport.split()  # Split long string into list of substrings

    # Split list into dict yee haw
    parsed_passport = {}
    for item in passport:
        key = item[:3]
        value = item[4:]
        parsed_passport[key] = value

    if not is_valid_byr(parsed_passport["byr"]):
        return False

    if not is_valid_iyr(parsed_passport["iyr"]):
        return False

    if not is_valid_eyr(parsed_passport["eyr"]):
        return False

    if not is_valid_hgt(parsed_passport["hgt"]):
        return False

    if not is_valid_hcl(parsed_passport["hcl"]):
        return False

    if not is_valid_ecl(parsed_passport["ecl"]):
        return False

    if not is_valid_pid(parsed_passport["pid"]):
        return False

    return True


def is_valid_byr(byr: str) -> bool:
    """
    (Birth Year) - four digits; at least 1920 and at most 2002.

    :return: Status of field (true = valid).
    :rtype: bool
    """
    byr = int(byr)
    if byr < 1920 or byr > 2002:
        return False
    return True


def is_valid_iyr(iyr: str) -> bool:
    """
    (Issue Year) - four digits; at least 2010 and at most 2020.

    :return: Status of field (true = valid).
    :rtype: bool
    """
    iyr = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False
    return True


def is_valid_eyr(eyr: str) -> bool:
    """
    (Expiration Year) - four digits; at least 2020 and at most 2030.

    :return: Status of field (true = valid).
    :rtype: bool
    """
    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False
    return True


def is_valid_hgt(hgt: str) -> bool:
    """
    (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.

    :return: Status of field (true = valid).
    :rtype: bool
    """
    units = hgt[-2:]
    if units not in ["in", "cm"]:
        return False
    hgt = int(hgt[:-2])
    if units == "in":
        if hgt < 59 or hgt > 76:
            return False
    if units == "cm":
        if hgt < 150 or hgt > 193:
            return False
    return True


def is_valid_hcl(hcl: str) -> bool:
    """
    (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

    :return: Status of field (true = valid).
    :rtype: bool
    """
    if hcl[0] != "#":
        return False
    if len(hcl[1:]) != 6:
        return False
    return True


def is_valid_ecl(ecl: str) -> bool:
    """
    (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

    :return: Status of field (true = valid).
    :rtype: bool
    """
    colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl not in colours:
        return False
    return True


def is_valid_pid(pid: str) -> bool:
    """
    (Passport ID) - a nine-digit number, including leading zeroes.

    :return: Status of field (true = valid).
    :rtype: bool
    """
    if len(pid) != 9:
        return False
    return True


if __name__ == "__main__":
    main()
