def day3_part1_v1(data):
    prio = {
        **{chr(n): n - ord('a') + 1 for n in range(ord('a'), ord('z') + 1)},
        **{chr(n): n - ord('A') + 27 for n in range(ord('A'), ord('Z') + 1)}
    }
    items = [set(r[:len(r)//2]).intersection(set(r[len(r)//2:])).pop() for r in data]
    return sum(prio[i] for i in items)


def main(f):
    data = open(f).read().splitlines()
    print(day3_part1_v1(data))


if __name__ == "__main__":
    main('day3_sample.txt')
    main('day3_input.txt')
