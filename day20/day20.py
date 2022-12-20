data = open("input.txt", "r").read().strip().split("\n")


# kind of hacky, using a wrapper class to differentiate duplicate values by index
class Node:
    def __init__(self, value: int, i: int):
        self.value = value
        self.i = i


def mix(nums: list[Node], iterations=1):
    original = nums.copy()

    for _ in range(iterations):
        for num in original:
            i = nums.index(num)
            nums.pop(i)
            j = (i + num.value) % len(nums)
            if j == 0:
                j = len(nums)
            nums.insert(j, num)

    return nums


def get_coords_sum(nums: list[Node]):

    zero_index = None

    for i in range(len(nums)):
        if nums[i].value == 0:
            zero_index = i
            break
    res = 0
    for val in [1000, 2000, 3000]:
        assert zero_index != None
        j = (zero_index + val) % len(nums)
        res += nums[j].value
    return res


def part_one(data: list[str]) -> int:
    nums = [Node(int(x), i) for i, x in enumerate(data)]
    nums = mix(nums, iterations=1)
    return get_coords_sum(nums)


def part_two(data: list[str]) -> int:
    key = 811589153
    nums = [Node(int(x) * key, i) for i, x in enumerate(data)]
    nums = mix(nums, iterations=10)
    return get_coords_sum(nums)


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
