from aoc2024.util import get_input


def make_lists(entries):
    left = list()
    right = list()
    for entry in entries:
        l, r = entry.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    return (left, right)


def solve_part1(entries):
    result = 0
    left, right = make_lists(entries)
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    return result


def solve_part2(entries):
    result = 0
    left, right = make_lists(entries)
    for i in left:
        result += i * right.count(i)
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day01/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
