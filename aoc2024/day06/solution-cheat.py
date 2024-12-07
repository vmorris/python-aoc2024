# Day 6: Guard Gallivant

from collections import defaultdict

import os


def get_input_path(path: str) -> str:
    base = os.path.dirname(__file__)
    return os.path.join(base, path)


def input_lines(path: str) -> list[str]:
    path = get_input_path(path)
    with open(path, "r") as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())

        return lines


inp = input_lines("input")

SZ = 130

dirmap = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
dirs = ("^", ">", "v", "<")

visited = set()  # keep track of all positions visited
field = {}  # after prep, field contains the lab map


def prep():
    """
    This builds an entirely new view of the lab without the guard's position or location and stores in "field'.
    The guard's X and Y position is returned. This assumes that the guard will always start facing north.

    """
    guard_x, guard_y = 0, 0
    for i, line in enumerate(inp):
        for j, c in enumerate(line):
            field[(j, i)] = "#" if c == "#" else "."
            if c == "^":
                guard_x, guard_y = j, i

    return guard_x, guard_y


def star1():
    # global visited  # this was defined, but I don't think it is necessary... we'll see.

    guard_x, guard_y = prep()
    guard_face = "^"

    # record the starting position
    visited.add((guard_x, guard_y))

    while True:
        dt = dirmap[dirs[gc]]
        dx, dy = gx + dt[0], gy + dt[1]
        if dx not in range(SZ) or dy not in range(SZ):
            break

        if field[(dx, dy)] == "#":
            gc = (gc + 1) % 4
        else:
            gx, gy = dx, dy

        visited.add((gx, gy))

    return len(visited)


def star2():
    global visited
    ox, oy = prep()

    total = 0
    for i, j in visited:
        if field[(i, j)] in ("#", "^") or (i == ox and j == oy):
            continue

        f = field.copy()
        f[(i, j)] = "#"

        trapped = False

        gx, gy, gc = ox, oy, 0
        visited = {(gx, gy)}

        assoc = defaultdict(set)
        watch = None
        while True:
            dt = dirmap[dirs[gc]]
            dx, dy = gx + dt[0], gy + dt[1]
            if dx not in range(SZ) or dy not in range(SZ):
                break

            if f[(dx, dy)] == "#":
                gc = (gc + 1) % 4
            else:
                assoc[(gx, gy)].add((dx, dy))
                gx, gy = dx, dy

            p = (gx, gy)
            if watch and p in watch:
                trapped = True
                break
            else:
                watch = None

            if p in assoc:
                watch = assoc[p].copy()

            visited.add((gx, gy))

        if trapped:
            total += 1

    return total


if __name__ == "__main__":
    print(star1())
    print(star2())
