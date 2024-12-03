from aoc2024.day03 import solution
from aoc2024.util import get_input


p1_input_data = get_input("tests/testinput.day03.part1", type="raw")
p2_input_data = get_input("tests/testinput.day03.part2", type="raw")


def test_solve_part1():
    expected = 161
    actual = solution.solve_part1(p1_input_data)
    assert expected == actual


def test_solve_part2():
    expected = 48
    actual = solution.solve_part2(p2_input_data)
    assert expected == actual
