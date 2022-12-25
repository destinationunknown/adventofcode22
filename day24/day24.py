from collections import deque

data = open("input.txt", "r").read().strip().split("\n")


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul_pair(a: tuple[int, int], b: tuple[int, int]):
    return (a[0] * b[0], a[1] * b[1])


def mod_pair(a, b):
    return (a[0] % b[0], a[1] % b[1])


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]

blizz_map = {"^": 0, "v": 1, "<": 2, ">": 3}


def parse_input(data: list[str]):
    blizzards = tuple(set() for _ in range(4))

    for i, row in enumerate(data[1:]):
        for j, val in enumerate(row[1:]):
            if val in blizz_map:
                blizzards[blizz_map[val]].add((i, j))

    rows = len(data) - 2
    cols = len(data[0]) - 2
    return blizzards, rows, cols


def valid(pos, t, blizzards, rows, cols):
    row, col = pos
    if pos == (-1, 0) or pos == (rows, cols - 1):
        return True
    if not 0 <= row < rows or not 0 <= col < cols:
        return False
    for index, direction in enumerate(directions):
        dr, dc = direction
        if ((row - (dr * t)) % rows, (col - (dc * t)) % cols) in blizzards[index]:
            return False
    return True


def get_neighbours(pos, t, blizzards, rows, cols):
    neighbours = {add_pair(pos, d) for d in directions}
    neighbours.add(pos)

    neighbours = {x for x in neighbours if valid(x, t, blizzards, rows, cols)}
    return neighbours


def bfs(start, end, start_time, blizzards, rows, cols):

    seen = set()

    q = deque([(start_time, start)])
    while q:
        t, pos = q.popleft()
        if pos == end:
            return t

        t += 1
        if (t, pos) in seen:
            continue

        seen.add((t, pos))
        for neighbour in get_neighbours(pos, t, blizzards, rows, cols):
            q.append((t, neighbour))

    return -1


def part_one(data: list[str]) -> int:
    blizzards, rows, cols = parse_input(data)
    start = (-1, 0)
    end = (rows, cols - 1)

    t = bfs(start, end, 0, blizzards, rows, cols)
    return t


def part_two(data: list[str]) -> int:
    blizzards, rows, cols = parse_input(data)
    start = (-1, 0)
    end = (rows, cols - 1)

    t1 = bfs(start, end, 0, blizzards, rows, cols)
    t2 = bfs(end, start, t1, blizzards, rows, cols)
    t3 = bfs(start, end, t2, blizzards, rows, cols)

    return t3


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
