import operator
from sympy import Eq, solve, sympify, Symbol

data = open("input.txt", "r").read().strip().split("\n")

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}


def part_one(data: list[str]) -> int:
    monkeys = [line.split(" ") for line in data]
    jobs = []

    vals = {}

    for line in monkeys:
        monkey = line[0][:-1]
        if len(line) == 2:
            val = int(line[1])
            vals[monkey] = val

        else:
            a = line[1]
            op = line[2]
            b = line[3]

            jobs.append((monkey, (a, b), op))

    while len(jobs) > 0:
        job = jobs.pop(0)
        m, (a, b), op = job
        if a in vals and b in vals:
            vals[m] = ops[op](vals[a], vals[b])
        else:
            jobs.append(job)

    return vals["root"]


def part_two(data: list[str]) -> int:
    monkeys = [line.split(" ") for line in data]
    jobs = []

    vals = {}

    for line in monkeys:
        monkey = line[0][:-1]
        if len(line) == 2:
            val = line[1]
            vals[monkey] = val

        else:
            a = line[1]
            op = line[2]
            b = line[3]

            jobs.append((monkey, (a, b), op))

    while len(jobs) > 0:
        vals["humn"] = "x"
        job = jobs.pop(0)
        m, (a, b), op = job
        if m == "root":
            op = "="
        if a in vals and b in vals:
            vals[m] = f"({vals[a]} {op} {vals[b]})"
        else:
            jobs.append(job)

    lhs, rhs = vals["root"].split("=")
    lhs = sympify(lhs[1:])
    rhs = sympify(rhs[:-1])
    eq = Eq(lhs, rhs)
    return solve(eq, Symbol("x"))[0]


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
