data = open('input.txt', 'r').read().strip().split("\n")

def part_one(data: list[str]):
    max_calories = 0
    current_calories = 0
    for line in data:
        if line == "":
            current_calories = 0
        else:
            calories = int(line)
            current_calories += calories
        max_calories = max(max_calories, current_calories)

    return max_calories


def part_two(data: list[str]):
    elfs = []
    current_calories = 0
    for line in data:
        if line == "":
            elfs.append(current_calories)
            current_calories = 0
        else:
            calories = int(line)
            current_calories += calories

    elfs.sort(reverse=True)
    return sum(elfs[0:3])


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
