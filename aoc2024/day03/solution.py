from aoc2024.util import get_input


import re


def find_next_instruction(index, text):
    """Given an index into text, find the next index of the next interesting instruction and return the match"""
    # Define the regex pattern for all interesting instructions
    pattern = r"don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\)"
    # Search for the next match after the given index
    match = re.search(pattern, text[index:])
    # If a match is found, return the pattern
    if match:
        return match
    return None  # No more matches found


def solve_part1(entries):
    index = 0
    instruction = find_next_instruction(index, entries)
    result = 0
    while instruction:
        if instruction.group().startswith("mul("):
            result += int(instruction[1]) * int(instruction[2])
        index += instruction.end()
        instruction = find_next_instruction(index, entries)
    return result


def solve_part2(entries):
    index = 0
    do_multiply = True
    instruction = find_next_instruction(index, entries)
    result = 0
    while instruction:
        if instruction.group() == "don't()":
            do_multiply = False
        elif instruction.group() == "do()":
            do_multiply = True
        elif instruction.group().startswith("mul("):
            if do_multiply:
                result += int(instruction[1]) * int(instruction[2])
        index += instruction.end()
        instruction = find_next_instruction(index, entries)
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day03/input", type="raw")
    print(solve_part1(entries))
    print(solve_part2(entries))
