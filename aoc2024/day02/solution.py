from aoc2024.util import get_input


def is_safe(report):
    safe = True
    increasing = True
    if report[0] > report[1]:
        increasing = False
    level = report[0]
    for next_level in report[1:]:
        # check that we're still going in the same direction
        if (level > next_level and increasing) or (
            level < next_level and not increasing
        ):
            safe = False
            break
        # test difference is within permitted range
        diff = abs(level - next_level)
        if diff == 0 or diff > 3:
            safe = False
            break
        # prime for next iteration
        level = next_level
    return safe


def solve_part1(entries):
    result = 0
    for report in entries:
        if is_safe(report):
            result += 1
    return result


def solve_part2(entries):
    result = 0
    for report in entries:
        if is_safe(report):
            result += 1
        else:
            for i in range(len(report)):
                _r = report.copy()
                _r.pop(i)
                if is_safe(_r):
                    result += 1
                    break
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day02/input", type="int-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
