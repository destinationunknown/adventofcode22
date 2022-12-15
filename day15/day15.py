data = open("input.txt", "r").read().strip().split("\n")


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = [UP, DOWN, LEFT, RIGHT]


def parse_input(data: list[str]):
    sensors = []
    beacons = []
    for line in data:
        sensor_desc, beacon_desc = line.split(":")

        sensor_desc = sensor_desc.replace(",", "")
        sensor_desc = sensor_desc.split(" ")
        sensor_x = int(sensor_desc[2].split("=")[1])
        sensor_y = int(sensor_desc[3].split("=")[1])
        sensor = (sensor_x, sensor_y)
        sensors.append(sensor)

        beacon_desc = beacon_desc.replace(",", "").strip()
        beacon_desc = beacon_desc.split(" ")
        beacon_x = int(beacon_desc[4].split("=")[1])
        beacon_y = int(beacon_desc[5].split("=")[1])
        beacon = (beacon_x, beacon_y)
        beacons.append(beacon)

    return sensors, beacons


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


# print(get_radius((4, 4), 4))


def part_one(data: list[str]):
    Y_TO_CHECK = 2000000
    p = set()

    def get_impossible_pos(sensor, beacon):
        d = dist(sensor, beacon)
        if abs(Y_TO_CHECK - sensor[1]) > d:
            return set()
        points = get_radius(sensor, d)
        if beacon in points:
            points.remove(beacon)
        return points

    def get_radius(pos, d):
        points = set()
        x, y = pos
        for i in range(x - d, x + d + 1):
            if dist(pos, (i, Y_TO_CHECK)) <= d:
                points.add((i, Y_TO_CHECK))
        return points
        sensors, beacons = parse_input(data)
        for s, b in zip(sensors, beacons):
            print(s, b)
            p = p.union(get_impossible_pos(s, b))
        print("got points")
        return len([x for x in p if x[1] == Y_TO_CHECK])


def part_two(data: list[str]):
    ceil = 4000000
    floor = 0
    sensors, beacons = parse_input(data)

    def valid(pos):
        x, y = pos
        if not floor <= x <= ceil or not floor <= y <= ceil:
            return False

        for s, b in zip(sensors, beacons):
            if dist(s, pos) <= dist(s, b):
                return False
        return True

    def get_perimeter(pos, d):
        x, y = pos
        i_start = max(floor, x - d)
        i_end = min(ceil + 1, x + d + 1)
        for i in range(i_start, i_end):
            for j_sign in [-1, 1]:
                remaining_d = abs(d - abs(x - i))
                j = y + (remaining_d * j_sign)
                neighbours = [add_pair((i, j), d) for d in directions]
                neighbours = [x for x in neighbours if dist(pos, x) == d + 1]
                for n in neighbours:
                    if valid(n):
                        return n[0] * (ceil + n[1])

    for s, b in zip(sensors, beacons):
        print(s, b)
        r = get_perimeter(s, dist(s, b))
        if r:
            return r


if __name__ == "__main__":
    # print(part_one(data))
    print(part_two(data))
