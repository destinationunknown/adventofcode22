from functools import lru_cache
import sys

from networkx.convert_matrix import itertools

sys.setrecursionlimit(100000000)
data = open("input.txt", "r").read().strip().split("\n")


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

    @lru_cache(maxsize=None)
    def helper(node, time_left, opened: frozenset):
        if time_left <= 0:
            return 0
        else:
            results = [helper(n, time_left - 1, opened) for n in graph[node][1]]
            if node not in opened and graph[node][0] > 0:
                val = (time_left - 1) * graph[node][0]
                _opened = set(opened)
                _opened.add(node)
                results += [helper(node, time_left - 1, frozenset(_opened)) + val]
            return max(results)

    return helper("AA", 30, frozenset())


def part_two(data: list[str]):
    graph = parse_input(data)

    @lru_cache(maxsize=None)
    def helper(person, elephant, time_left, opened: frozenset):
        if time_left <= 0:
            return 0
        else:
            results = [
                helper(p, e, time_left - 1, opened)
                for p, e in itertools.product(graph[person][1], graph[elephant][1])
            ]
            if person not in opened and graph[person][0] > 0:
                _opened = set(opened)
                val = (time_left - 1) * graph[person][0]
                _opened.add(person)
                results += [
                    helper(person, e, time_left - 1, frozenset(_opened)) + val
                    for e in graph[elephant][1]
                ]
            if elephant not in opened and graph[elephant][0] > 0:
                _opened = set(opened)
                val = (time_left - 1) * graph[elephant][0]
                _opened.add(elephant)
                results += [
                    helper(p, elephant, time_left - 1, frozenset(_opened)) + val
                    for p in graph[person][1]
                ]
            return max(results)

    return helper("AA", "AA", 26, frozenset())


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
