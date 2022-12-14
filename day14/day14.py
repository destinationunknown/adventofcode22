data = open("input.txt", "r").read().strip().split("\n")

from ast import literal_eval


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def parse_rocks(data: list[str]):
    rocks_desc = [[literal_eval(x.strip()) for x in line.split("->")] for line in data]
    rocks = set()

    for line in rocks_desc:
        i = 0
        while i < len(line) - 1:
            curr = line[i]
            next = line[i + 1]

            start_x, end_x = sorted([curr[0], next[0]])
            for x in range(start_x, end_x + 1):
                rocks.add((x, curr[1]))

            start_y, end_y = sorted([curr[1], next[1]])
            for y in range(start_y, end_y + 1):
                rocks.add((curr[0], y))

            i += 1

    return rocks


def next_sand_pos(pos, rocks):
    x, y = pos
    dirs = [(0, 1), (-1, 1), (1, 1)]

    possible = [add_pair(pos, d) for d in dirs]
    possible = [x for x in possible if x not in rocks]
    if len(possible) == 0:
        return pos
    else:
        return possible[0]


def part_one(data: list[str]):
    rocks = parse_rocks(data)

    sand_start = (500, 0)

    lowest = max(pos[1] for pos in rocks)

    sand_pos = sand_start
    start_count = 0

    while True:
        next_pos = next_sand_pos(sand_pos, rocks)

        if next_pos == sand_pos:
            rocks.add(sand_pos)
            start_count += 1
            sand_pos = sand_start
        else:
            sand_pos = next_pos

        if next_pos[1] > lowest:
            return start_count


def part_two(data: list[str]):
    rocks = parse_rocks(data)

    sand_start = (500, 0)

    lowest = max(pos[1] for pos in rocks)

    floor = lowest + 2

    sand_pos = sand_start
    start_count = 0

    while True:
        next_pos = next_sand_pos(sand_pos, rocks)

        if next_pos == sand_start:
            return start_count + 1

        if next_pos == sand_pos or next_pos[1] == floor:
            rocks.add(sand_pos)
            start_count += 1
            sand_pos = sand_start
        else:
            sand_pos = next_pos


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
