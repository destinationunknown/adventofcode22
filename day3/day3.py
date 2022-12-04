data = open("input.txt", "r").read().strip().split("\n")

# data = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
#     "PmmdzqPrVvPwwTWBwg",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
#     "ttgJtRGJQctTZtZT",
#     "CrZsJsPPZsGzwwsLwLmpwMDw",
# ]


def priority(x: str):
    if x.islower():
        return ord(x) - 96
    else:
        return ord(x) - 38


def part_one(data: list[str]):

    total = 0

    for line in data:
        half = len(line) // 2
        a, b = set(line[:half]), set(line[half:])
        common = a.intersection(b)
        total += sum([priority(x) for x in common])

    return total


def part_two(data: list[str]):
    total = 0
    for i in range(0, len(data), 3):
        group = [set(line) for line in data[i : i + 3]]
        badge = set.intersection(*group).pop()
        total += priority(badge)

    return total


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
