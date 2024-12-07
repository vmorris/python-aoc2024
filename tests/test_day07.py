from aoc2024.day07 import solution
from aoc2024.util import get_input


input_data = get_input("tests/testinput.day07", type="dict-ints")


def test_solve_part1():
    expected = 3749
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = None
    actual = solution.solve_part2(input_data)
    assert expected == actual
