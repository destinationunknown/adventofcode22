import operator

data = open("test.txt", "r").read().strip().split("\n")

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}


def part_one(data: list[str]) -> int:
    monkeys = [line.split(" ") for line in data]

    # monkeys that are waiting for key
    waiting = {}

    # set of monkeys that key requires
    jobs = {}

    vals = {}

    for line in monkeys:
        monkey = line[0][:-1]
        if len(line) == 2:
            val = int(line[1])
            vals[monkey] = val

            if monkey in waiting:
                q = []
                q.append(waiting[monkey])

                while q:
                    satisfied = q.pop(0)
                    if all([dep in vals for dep in jobs[satisfied][0]]):
                        op = jobs[satisfied][1]
                        a = jobs[satisfied][0][0]
                        b = jobs[satisfied][0][1]

                        vals[satisfied] = op(vals[a], vals[b])
                        if satisfied in waiting:
                            q.append(waiting[satisfied])

        else:
            a = line[1]
            op = ops[line[2]]
            b = line[3]

            if a in vals and b in vals:
                vals[monkey] = op(vals[a], vals[a])
            else:
                jobs[monkey] = [(a, b), op]
                waiting[a] = monkey
                waiting[b] = monkey

    print([j for j in jobs if j not in vals])
    return vals["root"]
    return 0


def part_two(data: list[str]) -> int:
    ...


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
