from aoc2024.day04 import solution
from aoc2024.util import get_input


input_data = get_input("tests/testinput.day04", type="char-matrix")


def test_solve_part1():
    expected = 18
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 9
    actual = solution.solve_part2(input_data)
    assert expected == actual