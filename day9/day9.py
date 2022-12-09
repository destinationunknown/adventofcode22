from itertools import combinations

data = open("input.txt", "r").read().strip().split("\n")


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub_pair(a, b):
    return (a[0] - b[0], a[1] - b[1])


dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

diagonal_dirs = [add_pair(a, b) for (a, b) in combinations(dirs.values(), 2)]
all_dirs = list(dirs.values()) + diagonal_dirs


def is_touching(h, t):
    return t in [add_pair(h, d) for d in all_dirs]


def binarize(a):
    return tuple([x // abs(x) if x != 0 else 0 for x in a])


def part_one(data: list[str]):

    h = (0, 0)
    t = (0, 0)

    seen = set()
    seen.add(t)

    for line in data:
        dir, dist = line.split(" ")
        dir = dirs[dir]
        dist = int(dist)

        for _ in range(dist):
            h = add_pair(h, dir)
            if not is_touching(h, t):
                diff = sub_pair(h, t)
                t = add_pair(t, binarize(diff))
                seen.add(t)

    return len(seen)


def part_two(data: list[str]):

    knots = [(0, 0) for _ in range(10)]

    seen = set()
    seen.add(knots[-1])

    for line in data:
        dir, dist = line.split(" ")
        dir = dirs[dir]
        dist = int(dist)

        for _ in range(dist):
            knots[0] = add_pair(knots[0], dir)
            curr = knots[0]
            for i in range(1, len(knots)):
                next = knots[i]
                if not is_touching(curr, next):
                    diff = sub_pair(curr, next)
                    knots[i] = add_pair(next, binarize(diff))
                curr = knots[i]
            seen.add(knots[-1])

    return len(seen)


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
