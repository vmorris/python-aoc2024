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
            """matrix, list of lists, strings split into chars"""
            result = list()
            for line in input:
                result.append([*line])
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
