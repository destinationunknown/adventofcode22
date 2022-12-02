data = open("input.txt", "r").read().strip().split("\n")

shape_scores = {"R": 1, "P": 2, "S": 3}
round_scores = {
    ("R", "R"): 3,
    ("R", "P"): 0,
    ("R", "S"): 6,
    ("P", "R"): 6,
    ("P", "P"): 3,
    ("P", "S"): 0,
    ("S", "R"): 0,
    ("S", "P"): 6,
    ("S", "S"): 3,
}


def part_one(data: list[str]):
    a = {"A": "R", "B": "P", "C": "S"}
    b = {"X": "R", "Y": "P", "Z": "S"}
    total_score = 0
    for line in data:
        their_move, my_move = line.split(" ")
        their_move = a[their_move]
        my_move = b[my_move]
        total_score += shape_scores[my_move] + round_scores[(my_move, their_move)]

    return total_score


def part_two(data: list[str]):
    a = {"A": "R", "B": "P", "C": "S"}
    b = {"X": "L", "Y": "D", "Z": "W"}
    matchup = {
        ("R", "W"): "P",
        ("R", "L"): "S",
        ("R", "D"): "R",
        ("P", "W"): "S",
        ("P", "L"): "R",
        ("P", "D"): "P",
        ("S", "W"): "R",
        ("S", "L"): "P",
        ("S", "D"): "S",
    }

    total_score = 0
    for line in data:
        their_move, outcome = line.split(" ")
        their_move = a[their_move]
        outcome = b[outcome]
        my_move = matchup[(their_move, outcome)]
        total_score += shape_scores[my_move] + round_scores[(my_move, their_move)]

    return total_score


if __name__ == "__main__":
    print(part_one(data))
    print(part_two(data))
