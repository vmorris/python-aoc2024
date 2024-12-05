from aoc2024.day05 import solution
from aoc2024.util import get_input


input_data = get_input("tests/testinput.day05", type="group_nlnl")
page_ordering_rules, updates = solution.process_input(input_data)


def test_solve_part1():
    expected = 143
    actual = solution.solve_part1(page_ordering_rules, updates)
    assert expected == actual


def test_solve_part2():
    expected = None
    actual = solution.solve_part2(page_ordering_rules, updates)
    assert expected == actual
