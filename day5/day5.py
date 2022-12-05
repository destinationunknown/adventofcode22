from collections import deque

data = open("input.txt", "r").read().strip().split("\n")


def part_one(data: list[str]):
    split = data.index("")

    stack_description, instructions = data[: split - 1], data[split + 1 :]
    stack_names = [int(x) for x in data[split - 1].split()]
    num_stacks = stack_names[-1]
    stacks = [deque() for _ in range(num_stacks)]

    for line in stack_description:
        for i in range(num_stacks):
            stack_index = i * 4 + 1
            stack = line[stack_index]
            if stack != " ":
                stacks[i].append(stack)

    for line in instructions:
        line = line.split(" ")
        count = int(line[1])
        source = int(line[3]) - 1
        dest = int(line[5]) - 1

        while count > 0 and len(stacks[source]) > 0:
            stack = stacks[source].popleft()
            stacks[dest].appendleft(stack)
            count -= 1

    res = ""
    for stack in stacks:
        res += stack[0]

    return res


def part_two(data: list[str]):
    split = data.index("")

    stack_description, instructions = data[: split - 1], data[split + 1 :]
    stack_names = [int(x) for x in data[split - 1].split()]
    num_stacks = stack_names[-1]
    stacks = [deque() for x in range(num_stacks)]

    for line in stack_description:
        for i in range(num_stacks):
            stack_index = i * 4 + 1
            stack = line[stack_index]
            if stack != " ":
                stacks[i].append(stack)

    for line in instructions:
        line = line.split(" ")
        count = int(line[1])
        source = int(line[3]) - 1
        dest = int(line[5]) - 1

        temp_stack = deque()

        while count > 0 and len(stacks[source]) > 0:
            stack = stacks[source].popleft()
            temp_stack.append(stack)
            count -= 1

        while len(temp_stack) > 0:
            stack = temp_stack.pop()
            stacks[dest].appendleft(stack)

    res = ""
    for stack in stacks:
        res += stack[0]

    return res


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
