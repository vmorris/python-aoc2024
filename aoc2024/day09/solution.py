import logging
import sys
from aoc2024.util import get_input

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)


sys.set_int_max_str_digits(20000)


class DataMap:
    def __init__(self):
        self.memory = []

    def add_block(self, block):
        self.memory.append(block)


class DataFile:
    def __init__(self, id: int, length: int):
        logger.info(f"creating file, id: {id}, length: {length}")
        self.id = id
        self.length = length

    def __repr__(self):
        return f"{str(self.id) * self.length}"


def expand_data(disk_map) -> str:
    result = []
    for index in range(len(disk_map)):
        if index % 2 == 0:
            file_id = index // 2
            file_length = int(disk_map[index])
            try:
                free_space = int(disk_map[index + 1])
            except IndexError:
                logger.info("INDEX ERROR")
                free_space = 0
            for _ in range(file_length):
                result.append(file_id)
            for _ in range(free_space):
                result.append(".")
    return result


def solve_part1(entries):
    expanded = expand_data(entries)
    logger.info(f"expanded: {expanded}")
    logger.info(
        f"Length of sparse data: {len(list(filter(lambda a: a != ".", expanded)))}"
    )
    right_index = len(expanded)
    for index in reversed(range(right_index)):  # iterate from the right
        # Last dot on the right or no dots left?  If so, we're done.
        dot_count = expanded.count(".")
        if dot_count == 0:
            logger.info("No more free space!")
            break
        char = expanded[index]
        # check for free space
        if char == ".":
            if dot_count == 1:  # just one free block left, we're done.
                logger.info("No more free space")
                expanded.pop(index)
                break
            else:  # not done, move to the left
                continue
        # get index of the first .
        dot_index = expanded.index(".")
        # move the data, dropping the "." off the end
        expanded = expanded[0:dot_index] + [char] + expanded[dot_index + 1 : index]
        logger.info(f" - MOVED {char} from {index} to {dot_index}")
        logger.info(expanded)
        logger.info(
            f"Length of sparse data: {len(list(filter(lambda a: a != ".", expanded)))}"
        )
    # truncated = expanded.rstrip(".")
    result = 0
    logger.info(
        f"Length of sparse data: {len(list(filter(lambda a: a != ".", expanded)))}"
    )
    logger.info(expanded)
    for index, file_id in enumerate(expanded):
        result += index * int(file_id)
        # logger.info(f"{result} = {index} * {file_id}")
    return result


def solve_part2(entries):
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day09/input", type="single_str")
    print(solve_part1(entries))
    print(solve_part2(entries))
