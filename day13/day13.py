import itertools
import math
import functools
import ast
import sys

sys.setrecursionlimit(900000000)

data = open("input.txt", "r").read().strip().split("\n")


def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            if a < b:
                return -1
            elif a > b:
                return 1
            return 0
        else:
            a = [a]
    if type(b) == int:
        if type(a) == int:
            if a < b:
                return -1
            elif a > b:
                return 1
            return 0
        else:
            b = [b]

    for i in range(min(len(a), len(b))):
        res = compare(a[i], b[i])
        if res != 0:
            return res
    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1
    return 0


def part_one(data: list[str]):
    pairs_desc = [
        list(y) for x, y in itertools.groupby(data, lambda z: z == "") if not x
    ]

    pairs = [[ast.literal_eval(p) for p in pair] for pair in pairs_desc]

    right_ordered = []

    for i, (left, right) in enumerate(pairs):
        if compare(left, right) < 0:
            right_ordered.append(i + 1)

    return sum(right_ordered)


def part_two(data: list[str]):
    divider_packets = [[[2]], [[6]]]
    packets = [ast.literal_eval(y) for y in data if y != ""]
    packets += divider_packets
    comp_key = functools.cmp_to_key(compare)
    packets.sort(key=comp_key)

    indices = [packets.index(d) + 1 for d in divider_packets]
    return math.prod(indices)


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
