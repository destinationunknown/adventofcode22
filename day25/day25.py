from functools import cache


data = open("input.txt", "r").read().strip().split("\n")


mapping = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


@cache
def pow5(n: int) -> int:
    return pow(5, n)


def parse_snafu(num: str) -> int:
    res = 0
    for index, char in enumerate(reversed(num)):
        digit = mapping[char] * pow5(index)
        res += digit
    return res


def make_snafu(num: int) -> str:
    curr = num
    res = ""
    while curr:
        digit = curr % 5

        if digit == 2:
            res = "2" + res
        elif digit == 1:
            res = "1" + res
        elif digit == 0:
            res = "0" + res
        elif digit == 4:
            res = "-" + res
            curr += 1
        elif digit == 3:
            res = "=" + res
            curr += 2
        curr = curr // 5

    return res


def part_one(data: list[str]) -> str:
    num_to_find = sum([parse_snafu(line) for line in data])
    return make_snafu(num_to_find)


if __name__ == "__main__":
    print(part_one(data))
