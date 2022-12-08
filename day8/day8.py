data = open("input.txt", "r").read().strip().split("\n")


def part_one(data: list[str]):
    grid = [list(map(int, [*line])) for line in data]
    counted = set()

    for row in range(len(data)):
        row_max = 0
        for col in range(len(data[row])):
            if col == 0 or col == len(data[row]) - 1 or grid[row][col] > row_max:
                counted.add((row, col))
            row_max = max(row_max, grid[row][col])

        row_max = 0
        for col in range(len(data[row]) - 1, -1, -1):
            if col == 0 or col == len(data[row]) - 1 or grid[row][col] > row_max:
                counted.add((row, col))
            row_max = max(row_max, grid[row][col])

    for col in range(len(data[0])):
        col_max = 0
        for row in range(len(data)):
            if row == 0 or row == len(data) - 1 or grid[row][col] > col_max:
                counted.add((row, col))
            col_max = max(col_max, grid[row][col])

        col_max = 0
        for row in range(len(data) - 1, -1, -1):
            if row == 0 or row == len(data) - 1 or grid[row][col] > col_max:
                counted.add((row, col))
            col_max = max(col_max, grid[row][col])

    return len(counted)


def part_two(data: list[str]):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    directions = [UP, DOWN, LEFT, RIGHT]
    grid = [list(map(int, [*line])) for line in data]

    def add_pair(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def in_grid(pos):
        row, col = pos
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])

    def continue_check(pos, height):
        row, col = pos
        return in_grid(pos) and grid[row][col] < height

    max_score = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            curr_score = 1
            for dir in directions:
                dist = 1
                pos = row, col
                new_pos = add_pair(pos, dir)
                height = grid[row][col]
                while continue_check(new_pos, height):
                    new_pos = add_pair(new_pos, dir)
                    dist += 1
                if not in_grid(new_pos):
                    dist -= 1

                curr_score *= dist
            max_score = max(max_score, curr_score)
    return max_score


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
