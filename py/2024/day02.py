from sys import argv

def check_report(report):
    unsafes = [] 
    inc = 0
    dec = 0
    prev = report[0]
    for value in report[1::]:
        if prev >= value: inc += 1
        if prev <= value: dec += 1
        unsafes.append((inc > 0 and dec > 0) or (inc == 0 and dec == 0) or abs(prev-value) > 3)
        prev = value
    return unsafes

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        grid = [[int(s) for s in line.split()] for line in file]

        part1 = 0
        part2 = 0
        for report in grid:
            unsafes = check_report(report)

            if not True in unsafes:
                part1 += 1
                part2 += 1
            else:
                for i in range(len(unsafes)+1):
                    if not True in check_report(report[:i]+report[i+1:]):
                        part2 += 1
                        break

        print("part1", part1)
        print("part2", part2)



