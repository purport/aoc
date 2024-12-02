from sys import argv

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        columns = [int(s) for line in file for s in line.split()]
        column1 = sorted(columns[0::2])
        column2 = sorted(columns[1::2])

        print("part1", sum([abs(a-b) for a,b in zip(column1, column2)]))

        nums = set(column1)
        print("part2", sum([a for a in column2 if a in nums]))

