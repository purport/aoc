from sys import argv


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        antennas = {}
        # locations = [[ch if ch == '2' or ch == '.' else '.' for ch in line.split()[0]] for line in file]
        locations = [[ch for ch in line.split()[0]] for line in file]
        antinodes =  [['.' for ch in line] for line in locations]
        for row, line in enumerate(locations):
            for col, loc in enumerate(line):
                if loc != '.':
                    antennas[loc] = antennas.get(loc, set())
                    antennas[loc].add((row,col))

        l = len(locations[0])
        part1 = 0
        part2 = 0
        for freq in antennas:
            locs = antennas[freq]
            for i, a1 in enumerate(locs):
                for j, a2 in enumerate(locs):
                    if i == j: continue
                    row1,col1=a1
                    row2,col2=a2
                    row = row2 - row1
                    col = col2 - col1
                    # if row < 0 and col < 0:
                    #     row = -row
                    #     col = -col
                    #     row1,col1,row2,col2 = row2,col2,row1,col1

                    index = 0
                    while True:
                        if 0 <= row2+row*index < l and 0 <= col2+col*index < l:
                            if antinodes[row2+row*index][col2+col*index] == '.':
                                antinodes[row2+row*index][col2+col*index] = '#'
                                if index == 1: part1 += 1
                                part2 += 1
                        else:
                            break
                        index += 1

                    index = 0
                    while True:
                        if 0 <= row1-row*index < l and 0 <= col1-col*index < l:
                            if antinodes[row1-row*index][col1-col*index] == '.':
                                antinodes[row1-row*index][col1-col*index] = '#'
                                if index == 1: part1 += 1
                                part2 += 1
                        else:
                            break
                        index += 1
            
        for line in antinodes: print(''.join(line))
        print('Part 1', part1)
        print('Part 2', part2)
