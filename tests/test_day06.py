from aoc2024.day06 import solution
from aoc2024.util import get_input


input_data = get_input("tests/testinput.day06", type="char-matrix")


def test_solve_part1():
    expected = 41
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 6
    actual = solution.solve_part2(input_data)
    assert expected == actual
