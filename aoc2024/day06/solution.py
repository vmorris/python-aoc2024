import copy
import logging
from multiprocessing import Pool
from aoc2024.util import get_input

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class Direction:
    def __init__(self, x, y, dirname):
        self.x = int(x)
        self.y = int(y)
        self.dirname = dirname

    def __repr__(self):
        return f"{self.dirname}"


DIRECTIONS = {
    "NORTH": Direction(0, -1, "^"),
    "EAST": Direction(1, 0, ">"),
    "SOUTH": Direction(0, 1, "v"),
    "WEST": Direction(-1, 0, "<"),
}


class Position:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"Position({self.x},{self.y})"

    def __add__(self, other: Direction):
        if type(other) != Direction:
            raise TypeError
        new_position = Position(self.x + other.x, self.y + other.y)
        return new_position

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))


def get_start(lab: list[list[str]]) -> tuple[Position, Direction]:
    """
    Given a map of the lab, locate the start position and direction
    """
    for y, row in enumerate(lab):
        for x, value in enumerate(row):
            match value:
                case "^":
                    position = Position(x, y)
                    direction = DIRECTIONS.get("NORTH")
                    return (position, direction)
                case ">":
                    position = Position(x, y)
                    direction = DIRECTIONS.get("EAST")
                    return (position, direction)
                case "v":
                    position = Position(x, y)
                    direction = DIRECTIONS.get("SOUTH")
                    return (position, direction)
                case "<":
                    position = Position(x, y)
                    direction = DIRECTIONS.get("WEST")
                    return (position, direction)
    raise ValueError


class GuardRoute:
    def __init__(self, lab):
        self.lab = lab
        self.position = None
        self.direction = None
        self.obstruction = "#O"
        self.position, self.direction = get_start(self.lab)
        self.path = list()
        self.new_obstruction = None

    def __repr__(self):
        if self.new_obstruction:
            return f"[GuardRoute mod {self.new_obstruction}]"
        else:
            return f"[GuardRoute original]"

    def set_new_obstruction(self, position: Position):
        self.new_obstruction = position
        self.lab[position.y][position.x] = "O"

    def step(self):
        # mark position visited
        self.lab[self.position.y][self.position.x] = "X"
        # record our current position in the path for loop lookup
        self.path.append(f"{self.position.x},{self.position.y},{self.direction}")
        # look ahead
        next_step = self.position + self.direction
        next_direction = self.direction
        # detect obstruction
        if self.lab[next_step.y][next_step.x] in self.obstruction:
            # turn right
            match self.direction.dirname:
                case "^":
                    next_direction = DIRECTIONS.get("EAST")
                case ">":
                    next_direction = DIRECTIONS.get("SOUTH")
                case "v":
                    next_direction = DIRECTIONS.get("WEST")
                case "<":
                    next_direction = DIRECTIONS.get("NORTH")
        # detect edge of map
        next_step = self.position + next_direction
        if not (
            0 <= next_step.x < len(self.lab[0]) and 0 <= next_step.y <= len(self.lab)
        ):
            raise IndexError
        # check the path history for previous visits
        lookup = f"{next_step.x},{next_step.y},{next_direction}"
        if lookup in self.path:
            # we've already been there
            return "looped"

        else:
            # take the step
            self.position = next_step
            self.direction = next_direction


def solve_part1(entries):
    map_copy = copy.deepcopy(entries)
    route = GuardRoute(map_copy)
    try:
        while True:
            route.step()
    except IndexError:
        pass
    result = 0
    for row in route.lab:
        for value in row:
            if value == "X":
                result += 1
    return result


def test_for_loop(route: GuardRoute):
    try:
        while True:
            if route.step() == "looped":
                return True
    except IndexError:
        return False


def solve_part2(entries):
    map_copy = copy.deepcopy(entries)
    original_route = GuardRoute(map_copy)
    try:
        while True:
            original_route.step()
    except IndexError:
        pass
    # drop starting location from original path
    test_path = original_route.path[1:]
    # create array of test routes
    obstructions = set()
    for location in test_path:
        x, y, _ = location.split(",")
        obstructions.add(Position(x, y))
    test_routes = list()
    for obs in obstructions:
        test_map = copy.deepcopy(entries)
        route = GuardRoute(test_map)
        route.set_new_obstruction(obs)
        test_routes.append(route)
    # test for loops with new obstructions along the path
    with Pool(10) as p:
        results = p.map(test_for_loop, test_routes)
    return sum([x for x in results])


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day06/input", type="char-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
