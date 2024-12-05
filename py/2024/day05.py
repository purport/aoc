from sys import argv


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        rules1 = {}
        for line in file:
            if len(line.strip()) == 0: break
            [before, after] = [int(s) for s in line.split('|')]
            rules1[before] = rules1.get(before, set())
            rules1[before].add(after)
        
        lines = [[int(s) for s in line.split(',')] for line in file]
        part1 = 0
        part2 = 0
        for line in lines:
            l = len(line)
            r = set()
            ok = True
            for after in line[::-1]:
                ok = ok and (after not in r)
                r = r | rules1[after]

            if ok:
                part1 += line[int((l-1)/2 if l%2==1 else (l/2))]
            else:
                while True:
                    r = set()
                    ok = True
                    for i in range(len(line), 0, -1):
                        after = line[i-1]
                        ok = ok and (after not in r)
                        if not ok:
                            swap = line[i]
                            line[i] = after
                            line[i-1] = swap
                            break
                        r = r | rules1[after]
                    if ok: break
                part2 += line[int((l-1)/2 if l%2==1 else (l/2))]

        print('Part 1', part1)
        print('Part 2', part2)

