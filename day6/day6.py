from collections import defaultdict


data = open("input.txt", "r").read().strip().split("\n")[0]


def part_one(data: str):
    chars = defaultdict(int)
    unique_count = 0

    for i in range(4):
        char = data[i]
        if chars[char] == 0:
            unique_count += 1
        chars[char] += 1

    if unique_count == 4:
        return 3

    i = 4
    while i < len(data):
        new_char = data[i]
        if chars[new_char] == 0:
            unique_count += 1
        chars[new_char] += 1

        removed_char = data[i - 4]
        if chars[removed_char] == 1:
            unique_count -= 1
        chars[removed_char] -= 1

        i += 1
        if unique_count == 4:
            return i


def part_two(data: str):
    chars = defaultdict(int)
    unique_count = 0

    for i in range(14):
        char = data[i]
        if chars[char] == 0:
            unique_count += 1
        chars[char] += 1

    if unique_count == 14:
        return 13

    i = 14
    while i < len(data):
        new_char = data[i]
        if chars[new_char] == 0:
            unique_count += 1
        chars[new_char] += 1

        removed_char = data[i - 14]
        if chars[removed_char] == 1:
            unique_count -= 1
        chars[removed_char] -= 1

        i += 1
        if unique_count == 14:
            return i


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
