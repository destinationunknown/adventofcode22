data = open("input.txt", "r").read().strip().split("\n")


def part_one(data: list[str]):
    i = 0
    cycle = 0
    x = 1
    adding = False
    val = 0

    strengths = []
    while i < len(data):
        cycle += 1

        if cycle % 40 == 20:
            strengths.append(cycle * x)

        if adding:
            x += val
            adding = False
        else:
            instruction = data[i].split(" ")
            op = instruction[0]
            if op == "addx":
                adding = True
                val = int(instruction[1])
            i += 1
    return sum(strengths)


def part_two(data: list[str]):
    i = 0
    grid = [["." for _ in range(40)] for _ in range(6)]
    cycle = 0
    x = 1
    adding = False
    val = 0

    while i < len(data):
        cycle += 1

        crt_row = (cycle - 1) // 40
        crt_pos = (cycle - 1) % 40

        if crt_pos in [x, x - 1, x + 1]:
            grid[crt_row][crt_pos] = "█"

        if adding:
            x += val
            adding = False
        else:
            instruction = data[i].split(" ")
            op = instruction[0]
            if op == "addx":
                adding = True
                val = int(instruction[1])
            i += 1

        crt_pos += 1
        if crt_pos == 40:
            crt_row += 1
            crt_pos = 0

    res = ""
    for row in grid:
        res += "".join(row)
        res += "\n"

    return res


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
