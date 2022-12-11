import itertools
import operator

data = open("input.txt", "r").read().strip().split("\n")

ops = {"+": operator.add, "*": operator.mul}

p = 1


class Monkey:
    inspected: int
    items: list[int]

    def __init__(self, items, operation, test):
        self.inspected = 0
        self.items = items
        self.operation = operation
        self.test = test

    # return (updated worry val, monkey to throw to)
    def inspect(self, div_factor):
        self.inspected += 1
        item = self.items.pop(0)
        item = self.operation(item)
        item = item // div_factor
        global p
        item = item % p
        recv_monkey = self.test(item)

        res = (item, recv_monkey)
        return res


def parse(data: list[str]) -> list[Monkey]:
    monkeys_desc = [
        list(y) for x, y in itertools.groupby(data, lambda z: z == "") if not x
    ]

    monkeys = []

    for monkey in monkeys_desc:
        items = monkey[1][monkey[1].index(":") + 1 :]
        items = list(map(int, items.split(",")))

        op_desc = monkey[2][monkey[2].index("=") + 1 :].strip().split(" ")
        op = ops[op_desc[1]]
        op_val = op_desc[2]

        if op_val == "old":
            operation = lambda x, o=op: o(x, x)
        else:
            op_val = int(op_val)
            operation = lambda x, o=op, v=op_val: o(x, v)

        test_fun_mod = int(monkey[3].split(" ")[-1])
        global p
        p *= test_fun_mod
        test_fun = lambda x, t=test_fun_mod: x % t == 0

        test_true = int(monkey[4].split(" ")[-1])
        test_false = int(monkey[5].split(" ")[-1])

        test = lambda x, h=test_fun, t=test_true, f=test_false: t if h(x) else f

        monkeys.append(Monkey(items, operation, test))

    return monkeys


def part_one(data: list[str]):
    monkeys = parse(data)

    for _ in range(20):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            while len(monkey.items) > 0:
                item, next_monkey = monkey.inspect(3)
                monkeys[next_monkey].items.append(item)

    inspections = [m.inspected for m in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


def part_two(data: list[str]):
    monkeys = parse(data)

    for _ in range(10000):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            while len(monkey.items) > 0:
                item, next_monkey = monkey.inspect(1)
                monkeys[next_monkey].items.append(item)

    inspections = [m.inspected for m in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
