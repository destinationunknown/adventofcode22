#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations

data = open("input.txt", "r").read().split("\n")


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def get_elves(data: list[str]) -> set[tuple[int, int]]:
    elves = set()

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == "#":
                elves.add((i, j))
    return elves


def no_neighbours(
    pos: tuple[int, int], directions: set[tuple[int, int]], elves: set[tuple[int, int]]
):
    return len({add_pair(pos, d) for d in directions if add_pair(pos, d) in elves}) == 0


def get_triad(primary, secondary):
    return {primary} | {add_pair(primary, s) for s in secondary}


NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)
primary_directions = {NORTH, SOUTH, EAST, WEST}
diagonal_directions = {add_pair(a, b) for (a, b) in combinations(primary_directions, 2)}
all_directions = primary_directions | diagonal_directions
all_directions.remove((0, 0))


def part_one(data: list[str]) -> int:
    elves = get_elves(data)
    start = 0
    prop_checks = [
        (get_triad(NORTH, {EAST, WEST}), NORTH),
        (get_triad(SOUTH, {EAST, WEST}), SOUTH),
        (get_triad(WEST, {NORTH, SOUTH}), WEST),
        (get_triad(EAST, {NORTH, SOUTH}), EAST),
    ]

    for _ in range(10):
        # propose positions
        proposed = defaultdict(int)
        proposed_by = {}

        for elf in elves:
            if no_neighbours(elf, all_directions, elves):
                continue
            else:
                proposed_pos = None
                for i in range(4):
                    dirs_to_check, dir_to_move = prop_checks[(start + i) % 4]

                    if no_neighbours(elf, dirs_to_check, elves):
                        proposed_pos = add_pair(elf, dir_to_move)
                        break

                if proposed_pos:
                    proposed[proposed_pos] += 1
                    proposed_by[proposed_pos] = elf

        for pos in proposed:
            if proposed[pos] == 1:
                elves.remove(proposed_by[pos])
                elves.add(pos)

        start = (start + 1) % 4

    # get the rectangle
    min_row = min(elves, key=lambda x: x[0])[0]
    max_row = max(elves, key=lambda x: x[0])[0]
    min_col = min(elves, key=lambda x: x[1])[1]
    max_col = max(elves, key=lambda x: x[1])[1]

    l = max_col - min_col + 1
    h = max_row - min_row + 1

    total_tiles = l * h
    return total_tiles - len(elves)


def part_two(data: list[str]) -> int:
    elves = get_elves(data)
    start = 0
    prop_checks = [
        (get_triad(NORTH, {EAST, WEST}), NORTH),
        (get_triad(SOUTH, {EAST, WEST}), SOUTH),
        (get_triad(WEST, {NORTH, SOUTH}), WEST),
        (get_triad(EAST, {NORTH, SOUTH}), EAST),
    ]

    moved = True
    r = 0
    while moved:
        # propose positions
        proposed = defaultdict(int)
        proposed_by = {}

        for elf in elves:
            if no_neighbours(elf, all_directions, elves):
                continue
            else:
                proposed_pos = None
                for i in range(4):
                    dirs_to_check, dir_to_move = prop_checks[(start + i) % 4]

                    if no_neighbours(elf, dirs_to_check, elves):
                        proposed_pos = add_pair(elf, dir_to_move)
                        break

                if proposed_pos:
                    proposed[proposed_pos] += 1
                    proposed_by[proposed_pos] = elf

        moved = False
        for pos in proposed:
            if proposed[pos] == 1:
                moved = True
                elves.remove(proposed_by[pos])
                elves.add(pos)

        start = (start + 1) % 4
        r += 1

    return r


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
