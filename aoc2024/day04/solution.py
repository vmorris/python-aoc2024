from collections import namedtuple
import logging

from aoc2024.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Position = namedtuple("Position", ["x", "y"])


class Direction:
    def __init__(self, x, y, dirname):
        self.x = x
        self.y = y
        self.dirname = dirname

    def __repr__(self):
        return self.dirname


# Cardinal direcitons for traversing the puzzle grid (X, Y)
NORTH = Direction(0, -1, "NORTH")
NORTHEAST = Direction(1, -1, "NORTHEAST")
EAST = Direction(1, 0, "EAST")
SOUTHEAST = Direction(1, 1, "SOUTHEAST")
SOUTH = Direction(0, 1, "SOUTH")
SOUTHWEST = Direction(-1, 1, "SOUTHWEST")
WEST = Direction(-1, 0, "WEST")
NORTHWEST = Direction(-1, -1, "NORTHWEST")
DIRECTIONS = [NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST]


class XM_Search:
    """When "XM" is located, this class tracks the "X" position and "M" direction, and will determine if "XMAS" exists."""

    def __init__(self, X_position: Position, direction: Direction):
        self.X_position = X_position
        self.direction = direction

    def is_XMAS(self, grid) -> bool:
        len_y = len(grid)
        len_x = len(grid[0])
        # double check that we still have "XM"
        assert grid[self.X_position.y][self.X_position.x] == "X"
        M_position = Position(
            self.X_position.x + self.direction.x, self.X_position.y + self.direction.y
        )
        if M_position.x < 0 or M_position.y < 0:
            raise IndexError
        assert grid[M_position.y][M_position.x] == "M"
        # continue checking in the direction for "A"
        A_position = Position(
            M_position.x + self.direction.x, M_position.y + self.direction.y
        )
        if not (0 <= A_position.x < len_x) or not (0 <= A_position.y < len_y):
            logging.debug(f"{self} went out of bounds searching for A")
            return False
        if grid[A_position.y][A_position.x] != "A":
            logger.debug(f"{self} failed to find 'A' at {A_position}")
            return False
        # continue checking in the direction for "S"
        S_position = Position(
            A_position.x + self.direction.x, A_position.y + self.direction.y
        )
        if not (0 <= S_position.x < len_x) or not (0 <= S_position.y < len_y):
            logging.debug(f"{self} went out of bounds searching for S")
            return False
        if grid[S_position.y][S_position.x] != "S":
            logger.debug(f"{self} failed to find 'S' at {S_position}")
            return False
        logger.debug(f"{self} IS XMAS!")
        return True

    def __repr__(self):
        return f"[XM_Search: {self.X_position} {self.direction}]"


def solve_part1(grid):
    potentials = list()
    # Find occurrences of "X" in the grid
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            if letter == "X":
                X_position = Position(x, y)
                # then search around that position for "M", saving the potentials
                for direction in DIRECTIONS:
                    maybe_M = Position(
                        X_position.x + direction.x, X_position.y + direction.y
                    )
                    if not (0 <= maybe_M.x < len(row)) or not (
                        0 <= maybe_M.y < len(grid)
                    ):  # out of bounds searching for M
                        continue
                    if grid[maybe_M.y][maybe_M.x] == "M":
                        potentials.append(
                            XM_Search(X_position=X_position, direction=direction)
                        )
    return [p.is_XMAS(grid) for p in potentials].count(True)


def solve_part2(grid):
    len_y = len(grid)
    len_x = len(grid[0])
    # find occurrences of "A" in the grid
    potentials = list()
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            if letter == "A":
                potentials.append(Position(x, y))
    # search in the diagonals for 2 "M" and 2 "S"
    result = 0
    for p in potentials:
        logger.debug(f"A found at {p}.")
        north_letters = ""
        south_letters = ""
        for d in [NORTHWEST, NORTHEAST]:  # check north first
            maybe = Position(p.x + d.x, p.y + d.y)
            if 0 <= maybe.x < len_x and 0 <= maybe.y < len_y:  # stay in bounds
                north_letters += grid[maybe.y][maybe.x]
        for d in [SOUTHWEST, SOUTHEAST]:  # now check south
            maybe = Position(p.x + d.x, p.y + d.y)
            if 0 <= maybe.x < len_x and 0 <= maybe.y < len_y:  # stay in bounds
                south_letters += grid[maybe.y][maybe.x]
        # compare north and south
        logger.debug(f"north {north_letters}; south {south_letters}")
        # if north is all M and south is all S, or vise-versa, we can count and continue early
        if (north_letters == "MM" and south_letters == "SS") or (
            north_letters == "SS" and south_letters == "MM"
        ):
            result += 1
            continue
        sorted_north = sorted(north_letters)
        sorted_south = sorted(south_letters)
        if sorted_north != ["M", "S"] or sorted_south != ["M", "S"]:
            logger.debug(f"sorted failed: north {sorted_north}; south {sorted_south}")
            continue
        if north_letters[::-1] == south_letters:
            logger.debug(f"comparision failed on reverse")
            continue
        result += 1
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day04/input", type="char-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
