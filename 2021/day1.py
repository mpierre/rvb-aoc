# https://adventofcode.com/2021/day/1

def day1_part1_v1(d):
    increases = 0
    for i in range(len(d) - 1):
        if d[i + 1] > d[i]:
            increases += 1
    return increases


def day1_part1_v2(d):
    return sum([d[i + 1] > d[i] for i in range(len(d) - 1)])


def day1_part1_v3(d):
    return sum(x > y for x, y in zip(d[1:], d[:-1]))


def day2_part2_v1(d):
    sums = [sum(d[i:i+3]) for i in range(len(d)-2)]
    return day1_part1_v3(sums)


def main(f):
    data = [int(n) for n in open(f).read().splitlines()]
    print(day1_part1_v1(data))
    print(day1_part1_v2(data))
    print(day1_part1_v3(data))

    print(day2_part2_v1(data))


if __name__ == "__main__":
    main('day1_sample.txt')
    main('day1_input.txt')
