def get_input(f, type="str"):
    if type == "raw":
        result = open(f).read()
    elif type == "group_nlnl":
        # split on nlnl and then split on nl
        input = open(f).read()
        groups = input.rstrip().split("\n\n")
        result = list()
        for group in groups:
            result.append([line for line in group.split("\n")])
    elif type == "nlnl":
        input = open(f).read()
        groups = input.rstrip().split("\n\n")
        result = [line.rstrip().split("\n") for line in groups]
    else:
        input = [line.rstrip() for line in open(f)]
        if type == "str":
            """list of strings"""
            return input
        if type == "single_str":
            """just the one string"""
            return input[0]
        if type == "int":
            """list of integers"""
            return [int(i) for i in input]
        if type == "split":
            """list of lists, split on whitespace"""
            return [i.split() for i in input]
        if type == "csv":
            """list of lists, split on commas"""
            return [i.split(",") for i in input]
        if type == "int-matrix":
            """matrix, list of lists converted to integers"""
            result = list()
            for line in input:
                result.append([int(i) for i in line.split()])
        if type == "char-matrix":
            """matrix, 2D tuple, strings split into chars"""
            result = list()
            for line in input:
                result.append(tuple([*line]))
            result = tuple(result)
        if type == "dict-ints":
            """dictionary, keys and values are list of ints"""
            result = dict()
            for line in input:
                k, vals = line.split(":")
                result[int(k)] = list(map(int, vals.split()))
    return result


def divide_chunks(items, step):
    """Divide a list into smaller chunks"""
    start = 0
    end = len(items)
    for i in range(start, end, step):
        yield items[i : i + step]


class Point:
    def __init__(self, x, y, name=""):
        self.x = int(x)
        self.y = int(y)
        self.name = name

    def __repr__(self) -> str:
        return f"Point[{self.name}({self.x},{self.y})]"

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, scalar) -> "Point":
        """Scale a Point by a scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Cannot multiply a Point by {type(scalar)}")
        return Point(x=self.x * scalar, y=self.y * scalar)

    def __rmul__(self, scalar) -> "Point":
        """Right multiplication (to handle scalar * Point)."""
        return self.__mul__(scalar)

    def __eq__(self, other: "Point") -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))
