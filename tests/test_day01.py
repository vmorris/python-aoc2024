from aoc2024.day01 import solution
from aoc2024.util import get_input


input_data = get_input("tests/testinput.day01")


def test_solve_part1():
    expected = 11
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 31
    actual = solution.solve_part2(input_data)
    assert expected == actual
