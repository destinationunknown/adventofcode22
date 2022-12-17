data = open("input.txt", "r").read().strip()


def make_rock(type: int, pos: tuple):
    rock = []
    x, y = pos
    # type 0: horizontal line
    if type == 0:
        rock = [(x + i, y) for i in range(4)]
    # type 1: plus
    elif type == 1:
        rock = [(x + i, y + 1) for i in range(3)]
        rock += [(x + 1, y + i) for i in range(3)]
    # type 2: backwards L
    elif type == 2:
        rock = [(x + i, y) for i in range(3)]
        rock += [(x + 2, y + i) for i in range(3)]
    # type 3: vertical line
    elif type == 3:
        rock = [(x, y + i) for i in range(4)]
    elif type == 4:
        rock = [(x + i, y + j) for i in range(2) for j in range(2)]
    return set(rock)


def add_pair(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def move(rock: set[tuple[int, int]], dir: tuple[int, int]) -> set[tuple[int, int]]:
    return {add_pair(x, dir) for x in rock}


DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

jet = {"<": LEFT, ">": RIGHT}


def hit_wall(rock):
    return min(rock, key=lambda x: x[0])[0] < 0 or max(rock, key=lambda x: x[0])[0] >= 7


def hit_floor(rock):
    return min(rock, key=lambda x: x[1])[1] < 0


def get_highest(grid):
    return max(grid, key=lambda x: x[1])[1]


def part_one(data: str):
    jets = [jet[j] for j in data]
    grid = set()
    rock_type = 0
    highest = -1

    fallen_rocks = 0
    i = 0
    while fallen_rocks < 2022:
        rock = make_rock(rock_type, (2, highest + 4))
        rock_type = (rock_type + 1) % 5
        while True:
            # sideways movement
            j = jets[i]
            i = (i + 1) % len(jets)
            next = move(rock, j)

            if not hit_wall(next) and not next.intersection(grid):
                rock = next

            # downwards movement
            next = move(rock, DOWN)
            if not hit_floor(next) and not next.intersection(grid):
                rock = next
            else:
                grid = grid.union(rock)
                highest = get_highest(grid)
                fallen_rocks += 1
                break

    return highest + 1


def part_two(data: str):
    seen_states = {}
    jets = [jet[j] for j in data]
    grid = set()
    rock_type = 0
    highest = -1

    fallen_rocks = 0
    i = 0

    # height gained from cycle repeating
    height = 0

    rocks_to_fall = 1000000000000

    while fallen_rocks < rocks_to_fall:

        rock = make_rock(rock_type, (2, highest + 4))
        rock_type = (rock_type + 1) % 5
        while True:
            # sideways movement
            j = jets[i]
            i = (i + 1) % len(jets)
            next = move(rock, j)

            if not hit_wall(next) and not next.intersection(grid):
                rock = next

            # downwards movement
            next = move(rock, DOWN)
            if not hit_floor(next) and not next.intersection(grid):
                rock = next
            else:
                grid = grid.union(rock)
                highest = get_highest(grid)
                fallen_rocks += 1
                break

        # don't check for a cycle twice
        if not height:
            n = 50
            top_rows = {(x, highest - y) for (x, y) in grid if highest - y <= n}
            entry_key = (rock_type, i, frozenset(top_rows))
            if entry_key in seen_states:
                starting_highest, starting_fallen_rocks = seen_states[entry_key]
                cycle_length = fallen_rocks - starting_fallen_rocks
                cycle_size = highest - starting_highest

                # repeat the cycle as many times as possible while remaining under the threshold
                num_cycles = (rocks_to_fall - fallen_rocks) // cycle_length
                fallen_rocks = fallen_rocks + (cycle_length * num_cycles)

                # add the height gained from simulating the cycles at the end
                height = num_cycles * cycle_size
            else:
                entry_val = (highest, fallen_rocks)
                seen_states[entry_key] = entry_val

    return highest + 1 + height


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
