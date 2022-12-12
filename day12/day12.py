data = open("input.txt", "r").read().strip().split("\n")

import sys
from collections import deque

sys.setrecursionlimit(100000000)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def in_grid(pos, grid):
    row, col = pos
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


def to_int(x):
    if x == "S":
        x = "a"
    elif x == "E":
        x = "z"
    return ord(x) - 96


def can_move(a, b, grid):
    a_r, a_c = a
    b_r, b_c = b
    a = to_int(grid[a_r][a_c])
    b = to_int(grid[b_r][b_c])

    return b - a <= 1


def get_neighbours(pos, grid):
    neighbours = [
        add_pair(pos, d) for d in directions if in_grid(add_pair(pos, d), grid)
    ]
    neighbours = [x for x in neighbours if can_move(pos, x, grid)]
    return neighbours


def bfs(starts, grid):
    seen = set()
    q = deque([(start, 0) for start in starts])
    while q:
        pos, d = q.popleft()
        if grid[pos[0]][pos[1]] == "E":
            return d
        elif pos in seen:
            continue
        else:
            seen.add(pos)
            for neighbour in get_neighbours(pos, grid):
                q.append((neighbour, d + 1))


def part_one(data: list[str]):
    grid = [[*line] for line in data]

    for r in range(len(data)):
        for c in range(len(data[r])):
            if grid[r][c] == "S":
                return bfs([(r, c)], grid)


def part_two(data: list[str]):
    grid = [[*line] for line in data]

    s = []
    for r in range(len(data)):
        for c in range(len(data[r])):
            if grid[r][c] == "S" or grid[r][c] == "a":
                s.append((r, c))

    return bfs(s, grid)


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
