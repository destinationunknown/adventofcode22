import re


data = open("input.txt", "r").read().split("\n")


def make_grid(data: list[str]):
    tiles = set()
    walls = set()

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == ".":
                tiles.add((i, j))
            elif val == "#":
                walls.add((i, j))
    return tiles, walls


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, RIGHT, DOWN, LEFT]


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul_pair(a, b):
    return (a[0] * b[0], a[1] * b[1])


def move(pos, direction, steps, tiles, walls):
    all_pos = tiles.union(walls)
    for _ in range(steps):
        next_pos = add_pair(pos, direction)
        if next_pos in tiles:
            pos = next_pos
        elif next_pos in walls:
            return pos
        else:
            # wrap around
            stat = direction.index(0)
            next_pos = min(
                {x for x in all_pos if x[stat] == pos[stat]},
                key=lambda x: sum(mul_pair(x, direction)),
            )
            if next_pos in walls:
                return pos
            else:
                pos = next_pos
    return pos


def next_direction(direction, turn: str) -> tuple[int, int]:
    i = directions.index(direction)
    if turn == "R":
        j = (i + 1) % 4

    elif turn == "L":
        j = (i - 1) % 4
    return directions[j]


def part_one(data: list[str]) -> int:
    tiles, walls = make_grid(data[:-3])
    instructions = re.split("([LR])", data[-2].strip())
    direction = RIGHT

    pos = min({x for x in tiles if x[0] == 0}, key=lambda x: x[1])

    for instruction in instructions:
        if instruction in ["L", "R"]:
            direction = next_direction(direction, instruction)
        else:
            steps = int(instruction)
            pos = move(pos, direction, steps, tiles, walls)

    row, col = pos
    facing = (directions.index(direction) - 1) % 4
    return ((row + 1) * 1000) + ((col + 1) * 4) + facing


def part_two(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
