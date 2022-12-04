data = open("input.txt", "r").read().strip().split("\n")


def part_one(data: list[str]):
    def range_overlap(a, b):
        return a[0] >= b[0] and a[1] <= b[1]

    count = 0
    for line in data:
        pair = line.split(",")
        pair = [list(map(int, x.split("-"))) for x in pair]

        if range_overlap(pair[0], pair[1]) or range_overlap(pair[1], pair[0]):
            count += 1

    return count


def part_two(data: list[str]):
    def range_overlap(a, b):
        return (a[0] >= b[0] and a[0] < b[1]) or (a[1] <= b[1] and a[1] >= b[0])

    count = 0
    for line in data:
        pair = line.split(",")
        pair = [list(map(int, x.split("-"))) for x in pair]

        if range_overlap(pair[0], pair[1]) or range_overlap(pair[1], pair[0]):
            count += 1

    return count


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
