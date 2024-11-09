from sys import argv

if __name__ ==  "__main__":
    column1 = []
    column2 = []
    with open(argv[1], 'r') as file:
        for line in file:
            splits = [int(s) for s in line.split()]
            column1.append(splits[0])
            column2.append(splits[1])
        column1.sort()
        column2.sort()

    part1 = 0
    for i in range(0, len(column1)):
        part1 += abs(column1[i] - column2[i])
    print("part1", part1)

    j = 0
    i = 0
    part2 = 0
    while i != len(column1) and j != len(column2):
        count = 0
        while j != len(column2) and column1[i] >= column2[j]:
            if column1[i] == column2[j]:
                count += 1 
            j += 1

        part2 += count*column1[i]

        current = i
        while i != len(column1) and column1[i] == column1[current]:
            i += 1

    print("part2", part2)

