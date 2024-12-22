from sys import argv

cache = {}
def possible(towels, a, towel=[]):
    if len(a) == 0:
        # print(towel)
        return 1
    if a in cache: return cache[a]

    count = 0
    for t in towels:
        if a.startswith(t):
            count += possible(towels, a[len(t):], [*towel, t])

    cache[a] = count
    return count

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        towels = []
        arrangements = []
        for index, line in enumerate(file):
            if index == 0:
                towels = [x.strip() for x in line.split(',')]
            elif index > 1:
                arrangements.append(line.strip())

        part1 = 0
        part2 = 0
        for a in arrangements:
            count = possible(towels, a)
            if count > 0: part1 += 1
            part2 += count

        print('Part 1', part1)
        print('Part 2', part2)

