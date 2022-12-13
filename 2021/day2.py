# https://adventofcode.com/2021/day/2

from functools import reduce

actions = {
    'forward': lambda p, n: (p[0] + n, p[1]),
    'down': lambda p, n: (p[0], p[1] + n),
    'up': lambda p, n: (p[0], p[1] - n),
}


def day2_part1_v1(data):
    pos = (0, 0)
    for row in data:
        direction, value = row.split()
        pos = actions[direction](pos, int(value))

    return pos[0] * pos[1]


def day2_part1_v2(data):
    pos = reduce(lambda p, r: actions[r[0]](p, int(r[1])), [r.split() for r in data], (0, 0))
    return pos[0] * pos[1]



actions2 = {
    'forward': lambda p, n: (p[0] + n, p[1] + (n*p[2]), p[2]),
    'down': lambda p, n: (p[0], p[1], p[2] + n),
    'up': lambda p, n: (p[0], p[1], p[2] - n),
}


def day2_part2_v1(data):
    pos = (0, 0, 0)  # x, y, aim
    for row in data:
        direction, value = row.split()
        pos = actions2[direction](pos, int(value))

    return pos[0] * pos[1]


def day2_part2_v2(data):
    rows = [r.split() for r in data]
    pos = reduce(lambda p, r: actions2[r[0]](p, int(r[1])), rows, (0, 0, 0))
    return pos[0] * pos[1]


def main(f):
    data = open(f).read().splitlines()
    print(day2_part1_v1(data))
    print(day2_part1_v2(data))
    
    print(day2_part2_v1(data))
    print(day2_part2_v2(data))


if __name__ == "__main__":
    main('day2_sample.txt')
    main('day2_input.txt')
