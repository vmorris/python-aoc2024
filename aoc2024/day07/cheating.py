from aoc2024.util import get_input


def part1(data):
    equations = []
    for line in data:
        print(line.split(":"))
        test_value, numbers = line.split(":")
        equations.append((int(test_value), [*map(int, numbers.strip().split())]))

    result = []

    for test_value, numbers in equations:
        possibles = [numbers.pop(0)]
        while numbers:
            curr = numbers.pop(0)
            temp = []
            for p in possibles:
                temp.append(p + curr)
                temp.append(p * curr)
            possibles = temp

        if test_value in possibles:
            result.append(test_value)

    return sum(result)


def part2(data):
    equations = []
    for line in data:
        test_value, numbers = line.split(":")
        equations.append((int(test_value), [*map(int, numbers.strip().split())]))

    result = []

    for test_value, numbers in equations:
        possibles = [numbers.pop(0)]
        while numbers:
            curr = numbers.pop(0)
            temp = []
            for p in possibles:
                next_values = [  # +, * and ||
                    p + curr,
                    p * curr,
                    int(str(p) + str(curr)),
                ]
                temp.extend([v for v in next_values if v <= test_value])
            possibles = temp

        if test_value in possibles:
            result.append(test_value)

    return sum(result)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day07/input", type="str")
    print(part1(entries))
    print(part2(entries))
