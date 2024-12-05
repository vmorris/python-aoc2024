from collections import defaultdict
import logging
from aoc2024.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_input(input):
    rules = defaultdict(list)
    for rule in input[0]:
        before, after = map(int, rule.split("|"))
        rules[before].append(after)
    updates = list()
    for update in input[1]:
        updates.append(list(map(int, update.split(","))))
    return (rules, updates)


def sort_updates(rules, updates):
    valid_updates = list()
    invalid_updates = list()
    for update in updates:
        valid = True
        logger.debug(f"checking update: {update}")
        for index, page in enumerate(update):
            logger.debug(f" - page: {page}")
            later_pages = set(update[index + 1 :])
            if not later_pages.issubset(set(rules[page])):
                logger.debug(f"{later_pages} not subset of {set(rules[page])}")
                valid = False
                break
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return (valid_updates, invalid_updates)


def solve_part1(rules, updates):
    result = 0
    valid_updates, _ = sort_updates(rules, updates)
    for update in valid_updates:
        mid_index = len(update) // 2
        result += update[mid_index]
    return result


def solve_part2(rules, updates):
    result = 0
    _, invalid_updates = sort_updates(rules, updates)
    for update in invalid_updates:
        logger.debug(f"p2: {update}")
        # i think the strat here is to find rule violations and then just swap the positions of the left and right values from the rule
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day05/input", type="group_nlnl")
    page_ordering_rules, updates = process_input(entries)
    print(solve_part1(page_ordering_rules, updates))
    print(solve_part2(page_ordering_rules, updates))
