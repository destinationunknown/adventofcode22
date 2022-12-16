import sys

sys.setrecursionlimit(100000000)
data = open("test.txt", "r").read().strip().split("\n")


def parse_input(data: list[str]):
    graph = {}
    for line in data:
        name = line.split(" ")[1]
        flow_rate = int(line[line.index("=") + 1 : line.index(";")])
        neighbours = line[line.index(";") + 24 :].strip().replace(" ", "").split(",")
        graph[name] = (flow_rate, neighbours)
    return graph


def part_one(data: list[str]):
    graph = parse_input(data)
    print(graph)

    def helper(node, time, opened):
        opened = opened.copy()
        if time <= 0:
            # calculate the value of this path
            pressure = sum([(opened[valve]) * graph[valve][0] for valve in opened])
            return pressure
        else:
            results = [helper(n, time - 1, opened) for n in graph[node][1]]
            if node not in opened and graph[node][0] > 0:
                opened[node] = time
                results += [helper(node, time - 1, opened)]
            return max(results)

            # if node not in opened and graph[node][0] > 0:
            #     time -= 1
            #     opened[node] = time

            # unexplored = [n for n in graph[node][1] if n not in opened]
            # if unexplored:
            #     next_node = max(unexplored, key=lambda x: graph[x][0])
            #     return helper(next_node, time - 1, opened)
            # else:
            # results = [helper(n, time - 1, opened) for n in graph[node][1]]
            return max(results)

    return helper("AA", 30, {})


def part_two(data: list[str]):
    ...


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
