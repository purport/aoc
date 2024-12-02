from sys import argv

def check_diffs(diffs):
    return all([-3 <= d < 0 for d in diffs]) or all([0 < d <= 3 for d in diffs])

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        grid = [[int(s) for s in line.split()] for line in file]

        part1 = 0
        part2 = 0
        for report in grid:
            diffs = [a-b for a, b in zip(report[0::], report[1::])]
            if check_diffs(diffs):
                part1 += 1
                part2 += 1
            else:
                for i in range(len(report)):
                    fixed = diffs.copy()
                    if i == 0:               del fixed[0]
                    elif i == len(report)-1: del fixed[-1]
                    else:                    fixed[i-1] += fixed.pop(i)

                    if check_diffs(fixed):
                        part2 += 1
                        break

        print("part1", part1)
        print("part2", part2)



