from collections import defaultdict


data = open("input.txt", "r").read().strip().split("\n")


def make_filesystem(data: list[str]) -> dict[tuple[str], int]:
    stack = []
    stack.append("/")
    dirs = defaultdict(int)

    for i in range(len(data)):
        line = data[i].split(" ")
        if line[0] == "$":
            command = line[1]
            if command == "cd":
                dir = line[2]
                if dir == "..":
                    stack.pop()
                elif dir == "/":
                    stack = []
                    stack.append("/")
                else:
                    stack.append(dir)

        else:
            if line[0] != "dir":
                for i in range(len(stack)):
                    dir = tuple(stack[: i + 1])
                    dirs[dir] += int(line[0])

    return dirs


def part_one(data: list[str]):
    dirs = make_filesystem(data)
    return sum([x for x in dirs.values() if x <= 100000])


def part_two(data: list[str]):
    dirs = make_filesystem(data)
    total_space = 70000000
    required_space = 30000000
    used_space = dirs[("/",)]
    space_to_delete = required_space - (total_space - used_space)
    return min([x for x in dirs.values() if x >= space_to_delete])


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
