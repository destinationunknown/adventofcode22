import functools
import sys

sys.setrecursionlimit(100000000)

data = open("test.txt", "r").read().strip().split("\n")


class Blueprint:
    def __init__(self, ore_cost, clay_cost, obsidian_cost, geode_cost):
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost
        self.geode_cost = geode_cost


def parse_input(data: list[str]):
    blueprints = []
    for line in data:
        blueprint = line[line.index(":") + 2 :].split(".")
        print(blueprint)

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
    blueprint: Blueprint,
) -> int:
    if minute > 24:
        return geode

    ore += ore_r
    clay += clay_r
    obsidian += obsidian_r
    geode += geode_r

    possibilities = []

    if ore >= blueprint.geode_cost[0] and obsidian >= blueprint.geode_cost[1]:
        possibilities.append(
            assess_blueprint(
                ore - blueprint.geode_cost[0],
                clay,
                obsidian - blueprint.geode_cost[1],
                geode,
                ore_r,
                clay_r,
                obsidian_r,
                geode_r + 1,
                minute - 1,
                blueprint,
            )
        )

    elif ore >= blueprint.obsidian_cost[0] and clay >= blueprint.obsidian_cost[1]:
        possibilities.append(
            assess_blueprint(
                ore - blueprint.obsidian_cost[0],
                clay - blueprint.obsidian_cost[1],
                obsidian,
                geode,
                ore_r,
                clay_r,
                obsidian_r + 1,
                geode_r,
                minute - 1,
                blueprint,
            )
        )

    elif clay >= blueprint.clay_cost:
        possibilities.append(
            assess_blueprint(
                ore,
                clay - blueprint.clay_cost,
                obsidian,
                geode,
                ore_r,
                clay_r + 1,
                obsidian_r,
                geode_r,
                minute - 1,
                blueprint,
            )
        )
    elif ore >= blueprint.ore_cost:
        possibilities.append(
            assess_blueprint(
                ore - blueprint.ore_cost,
                clay,
                obsidian,
                geode,
                ore_r + 1,
                clay_r,
                obsidian_r,
                geode_r,
                minute - 1,
                blueprint,
            )
        )
    possibilities.append(
        assess_blueprint(
            ore,
            clay,
            obsidian,
            geode,
            ore_r,
            clay_r,
            obsidian_r,
            geode_r,
            minute - 1,
            blueprint,
        )
    )

    return max(possibilities)


def part_one(data: list[str]):
    blueprints = parse_input(data)
    return assess_blueprint(0, 0, 0, 0, 1, 0, 0, 0, 1, blueprints[0])


def part_two(data: list[str]):
    ...


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
