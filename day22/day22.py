import re

data = open("input.txt", "r").read().split("\n")
FACE_SIZE = 50


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


def get_face(pos) -> int:
    row, col = pos
    if 0 <= row < FACE_SIZE:
        if FACE_SIZE <= col < (2 * FACE_SIZE):
            return 1
        elif (2 * FACE_SIZE) <= col < (3 * FACE_SIZE):
            return 2
        else:
            raise Exception()
    elif FACE_SIZE <= row < (2 * FACE_SIZE):
        if FACE_SIZE <= col < (2 * FACE_SIZE):
            return 3
        else:
            raise Exception()
    elif (2 * FACE_SIZE) <= row < (3 * FACE_SIZE):
        if 0 <= col < FACE_SIZE:
            return 4
        elif FACE_SIZE <= col < (2 * FACE_SIZE):
            return 5
        else:
            raise Exception()
    elif (3 * FACE_SIZE) <= row < (4 * FACE_SIZE):
        if 0 <= col < FACE_SIZE:
            return 6
        raise Exception()
    else:
        raise Exception()


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, RIGHT, DOWN, LEFT]


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul_pair(a, b):
    return (a[0] * b[0], a[1] * b[1])


def move(
    pos: tuple[int, int], direction: tuple[int, int], steps, tiles, walls
) -> tuple[tuple[int, int], tuple[int, int]]:
    for _ in range(steps):
        # print(pos)
        next_pos = add_pair(pos, direction)
        if next_pos in tiles:
            pos = next_pos
        elif next_pos in walls:
            return pos, direction
        else:
            # wrap around
            row, col = pos
            m_row, m_col = row % FACE_SIZE, col % FACE_SIZE
            next_row, next_col = -1, -1
            face = get_face(pos)
            next_direction = None

            if direction == UP:
                if face == 1:
                    # next face is 6
                    next_row = (3 * FACE_SIZE) + m_col
                    next_col = 0
                    next_direction = RIGHT

                if face == 2:
                    # next face is 6
                    next_row = (4 * FACE_SIZE) - 1
                    next_col = m_col
                    next_direction = UP

                if face == 4:
                    # next face is 3
                    next_row = FACE_SIZE + m_col
                    next_col = FACE_SIZE
                    next_direction = RIGHT

            elif direction == RIGHT:
                if face == 2:
                    # next face is 5
                    next_row = (3 * FACE_SIZE) - m_row - 1
                    next_col = (2 * FACE_SIZE) - 1
                    next_direction = LEFT

                if face == 3:
                    # next_face is 2
                    next_row = FACE_SIZE - 1
                    next_col = (2 * FACE_SIZE) + m_row
                    next_direction = UP

                if face == 5:
                    # next face is 2
                    next_row = FACE_SIZE - m_row - 1
                    next_col = (3 * FACE_SIZE) - 1
                    next_direction = LEFT

                if face == 6:
                    # next face is 5
                    next_row = (3 * FACE_SIZE) - 1
                    next_col = FACE_SIZE + m_row
                    next_direction = UP

            elif direction == DOWN:
                if face == 2:
                    # next face is 3
                    next_row = FACE_SIZE + m_col
                    next_col = (2 * FACE_SIZE) - 1
                    next_direction = LEFT

                if face == 5:
                    # next face is 6
                    next_row = (3 * FACE_SIZE) + m_col
                    next_col = FACE_SIZE - 1
                    next_direction = LEFT

                if face == 6:
                    # next face is 2
                    next_row = 0
                    next_col = (2 * FACE_SIZE) + m_col
                    next_direction = DOWN

            elif direction == LEFT:
                if face == 1:
                    # next face is 4
                    next_row = (3 * FACE_SIZE) - m_row - 1
                    next_col = 0
                    next_direction = RIGHT

                if face == 3:
                    # next face is 4
                    next_row = 2 * FACE_SIZE
                    next_col = m_row
                    next_direction = DOWN

                if face == 4:
                    # next face is 1
                    next_row = FACE_SIZE - m_row - 1
                    next_col = FACE_SIZE
                    next_direction = RIGHT

                if face == 6:
                    # next face is 1
                    next_row = 0
                    next_col = FACE_SIZE + m_row
                    next_direction = DOWN
            else:
                print("Unknown direction!")

            next_pos = (next_row, next_col)
            if next_pos in walls:
                return pos, direction
            else:
                pos = next_pos
                if next_direction == None:
                    print("next_direction was not set!")
                    print(pos)
                    exit()
                else:
                    direction = next_direction
            assert pos in tiles
    return pos, direction


def get_next_direction(direction, turn: str) -> tuple[int, int]:
    i = directions.index(direction)
    if turn == "R":
        j = (i + 1) % 4
    else:
        j = (i - 1) % 4
    return directions[j]


def part_one(data: list[str]) -> int:
    tiles, walls = make_grid(data[:-3])
    instructions = re.split("([LR])", data[-2].strip())
    direction = RIGHT

    pos = min({x for x in tiles if x[0] == 0}, key=lambda x: x[1])

    for instruction in instructions:
        if instruction in ["L", "R"]:
            direction = get_next_direction(direction, instruction)
        else:
            steps = int(instruction)
            pos, direction = move(pos, direction, steps, tiles, walls)

    row, col = pos
    facing = (directions.index(direction) - 1) % 4
    return ((row + 1) * 1000) + ((col + 1) * 4) + facing


def part_two(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
