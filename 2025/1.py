def read_input_from_file(file_path: str):
    with open(file_path, "r") as file:
        return file.readlines()


def solve_part1(lines):
    """
    Implement Day 1 Part 1 here.
    `lines` is a list of strings from input.txt (including trailing newlines).
    """
    ans = 0
    x = 50
    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            x -= distance
        elif direction == "R":
            x += distance
        
        if x > 99:
            x = (x) % 100
        if x < 0:
            x = (x ) % 100
        
        if x == 0:
            ans += 1


    return ans


def solve_part2(lines):
    """
    Count how many individual clicks (steps of 1 on the dial) land on 0.
    """
    ans = 0
    x = 50

    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        direction = line[0]
        distance = int(line[1:])

        step = -1 if direction == "L" else 1

        # Simulate each click of the dial.
        for _ in range(distance):
            x = (x + step) % 100
            if x == 0:
                ans += 1

    return ans


if __name__ == "__main__":
    # By default, read from input.txt at the repo root.
    lines = read_input_from_file("input.txt")

    # Print answers in a clear format Advent of Code style.
    print("Part 1:", solve_part1(lines))
    print("Part 2:", solve_part2(lines))


    lines = read_input_from_file("problem.txt")

    # Print answers in a clear format Advent of Code style.
    print("Part 1:", solve_part1(lines))
    print("Part 2:", solve_part2(lines))

