import functools
import math
import sys

sys.setrecursionlimit(100000000)

data = open("input.txt", "r").read().strip().split("\n")


class Blueprint:
    def __init__(self, ore_cost, clay_cost, obsidian_cost, geode_cost):
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost
        self.geode_cost = geode_cost

        # try to limit the state space by defining a max number of robots we could possibly need
        # if the amount of resources we gain in 1 min is more than the max amount of that resource we could spend in one minute,
        # we don't need any more robots
        self.max_ore_r = max(ore_cost, clay_cost, obsidian_cost[0], geode_cost[0])
        self.max_clay_r = obsidian_cost[1]
        self.max_obsidian_r = geode_cost[1]


def parse_input(data: list[str]):
    blueprints = []
    for line in data:
        blueprint = line[line.index(":") + 2 :].split(".")

        ore_cost = int(blueprint[0].strip().split(" ")[4])
        clay_cost = int(blueprint[1].strip().split(" ")[4])
        obsidian_cost = (
            int(blueprint[2].strip().split(" ")[4]),
            int(blueprint[2].strip().split(" ")[7]),
        )
        geode_cost = (
            int(blueprint[3].strip().split(" ")[4]),
            int(blueprint[3].strip().split(" ")[7]),
        )

        blueprints.append(Blueprint(ore_cost, clay_cost, obsidian_cost, geode_cost))
    return blueprints


@functools.lru_cache(maxsize=None)
def assess_blueprint(
    ore,
    clay,
    obsidian,
    geode,
    ore_r,
    clay_r,
    obsidian_r,
    geode_r,
    minute,
    max_time,
    blueprint: Blueprint,
) -> int:
    if minute > max_time:
        return geode

    # try to limit the state space by defining maximum amount of each possible resource we could use
    ore = min((max_time + 1 - minute) * blueprint.max_ore_r, ore)
    clay = min((max_time + 1 - minute) * blueprint.max_clay_r, clay)
    obsidian = min((max_time + 1 - minute) * blueprint.max_obsidian_r, obsidian)

    possibilities = []

    if ore >= blueprint.geode_cost[0] and obsidian >= blueprint.geode_cost[1]:
        possibilities.append(
            assess_blueprint(
                ore + ore_r - blueprint.geode_cost[0],
                clay + clay_r,
                obsidian + obsidian_r - blueprint.geode_cost[1],
                geode + geode_r,
                ore_r,
                clay_r,
                obsidian_r,
                geode_r + 1,
                minute + 1,
                blueprint,
            )
        )

    if (
        obsidian_r < blueprint.max_obsidian_r
        and ore >= blueprint.obsidian_cost[0]
        and clay >= blueprint.obsidian_cost[1]
    ):
        possibilities.append(
            assess_blueprint(
                ore + ore_r - blueprint.obsidian_cost[0],
                clay + clay_r - blueprint.obsidian_cost[1],
                obsidian + obsidian_r,
                geode + geode_r,
                ore_r,
                clay_r,
                obsidian_r + 1,
                geode_r,
                minute + 1,
                blueprint,
            )
        )

    if clay_r < blueprint.max_clay_r and ore >= blueprint.clay_cost:
        possibilities.append(
            assess_blueprint(
                ore + ore_r - blueprint.clay_cost,
                clay + clay_r,
                obsidian + obsidian_r,
                geode + geode_r,
                ore_r,
                clay_r + 1,
                obsidian_r,
                geode_r,
                minute + 1,
                blueprint,
            )
        )
    if ore_r < blueprint.max_ore_r and ore >= blueprint.ore_cost:
        possibilities.append(
            assess_blueprint(
                ore + ore_r - blueprint.ore_cost,
                clay + clay_r,
                obsidian + obsidian_r,
                geode + geode_r,
                ore_r + 1,
                clay_r,
                obsidian_r,
                geode_r,
                minute + 1,
                blueprint,
            )
        )

    possibilities.append(
        assess_blueprint(
            ore + ore_r,
            clay + clay_r,
            obsidian + obsidian_r,
            geode + geode_r,
            ore_r,
            clay_r,
            obsidian_r,
            geode_r,
            minute + 1,
            blueprint,
        )
    )

    return max(possibilities)


def part_one(data: list[str]):
    blueprints = parse_input(data)
    q = 0
    for i, blueprint in enumerate(blueprints):
        print(i)
        q += (i + 1) * assess_blueprint(0, 0, 0, 0, 1, 0, 0, 0, 1, 26, blueprint)
    return q


def part_two(data: list[str]):
    blueprints = parse_input(data)
    q = 1
    for i, blueprint in enumerate(blueprints[:3]):
        print(i)
        q *= assess_blueprint(0, 0, 0, 0, 1, 0, 0, 0, 1, 32, blueprint)
    return q


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
