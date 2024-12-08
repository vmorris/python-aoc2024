from collections import defaultdict
from itertools import combinations
import logging
from typing import Tuple, Dict
from aoc2024.util import get_input, Point

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Antenna:
    def __init__(self, frequency: str, location: Point):
        self.frequency: str = frequency
        self.location: Point = location

    def __add__(self, other: "Antenna") -> Tuple[Point]:
        """
        Adding two antennas together produces the antinode locations.
        """
        vector = Point(
            name=f"{self.frequency}_vector",
            x=(self.location.x - other.location.x),
            y=(self.location.y - other.location.y),
        )
        node1 = self.location + vector
        node2 = other.location - vector
        return (node1, node2)

    def __mul__(self, other: "Antenna") -> Tuple[Point]:
        """
        Multiplying two antennas together produces antinode locations
        along the line connecting the two antennas, stopping after collecting
        some number of antinodes in each direction.
        """
        STOP = 100
        result = list()
        vector = Point(
            name=f"{self.frequency}_vector",
            x=(self.location.x - other.location.x),
            y=(self.location.y - other.location.y),
        )
        # add the antenna locations to the result
        result.extend([self.location, other.location])
        # step in each direction, adding locations to the result
        node1 = self.location
        node2 = other.location
        for _ in range(STOP):
            node1 += vector
            node2 -= vector
            result.extend([node1, node2])
        return tuple(result)

    def __repr__(self):
        return f"Antenna[freq:{self.frequency}, loc:{self.location}]"


def collect_antennas(city_map) -> Dict:
    antennas = defaultdict(list)
    for y_index, row in enumerate(city_map):
        for x_index, frequency in enumerate(row):
            if frequency != ".":
                antenna = Antenna(frequency, Point(x_index, y_index))
                antennas[frequency].append(antenna)
    return antennas


def solve_part1(entries):
    antinodes = set()
    y_max = len(entries)
    x_max = len(entries[0])
    all_antennas = collect_antennas(entries)
    for _, antennas in all_antennas.items():
        pairs = list(combinations(antennas, 2))
        for p in pairs:
            anodes = p[0] + p[1]
            for node in anodes:
                if 0 <= node.x < x_max and 0 <= node.y < y_max:
                    antinodes.add(node)
    return len(antinodes)


def solve_part2(entries):
    antinodes = set()
    y_max = len(entries)
    x_max = len(entries[0])
    all_antennas = collect_antennas(entries)
    for _, antennas in all_antennas.items():
        pairs = list(combinations(antennas, 2))
        for p in pairs:
            anodes = p[0] * p[1]
            for node in anodes:
                if 0 <= node.x < x_max and 0 <= node.y < y_max:
                    antinodes.add(node)
    return len(antinodes)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day08/input", type="char-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
