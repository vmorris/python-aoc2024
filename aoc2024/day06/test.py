visited = set()


def star1():
    # global visited
    visited.add((1, 2))


def star2():
    global visited
    for i, j in visited:
        visited = {(1, 2)}
