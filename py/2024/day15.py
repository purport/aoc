from sys import argv

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        warehouse = []
        x = 0
        y = 0
        for line in file:
            if line.strip() == '':
                break
            row = [x for x in line.strip()]
            if '@' in row:
                x = row.index('@')
            if x == 0: y += 1
            warehouse.append(row)
        moves = ''
        for line in file:
            moves += line.strip()

        for index, move in enumerate(moves):
            if move == 'v':
                if warehouse[y+1][x] == '.':
                    y += 1
                    warehouse[y][x],warehouse[y-1][x] = warehouse[y-1][x],warehouse[y][x]
                elif warehouse[y+1][x] == '#':
                    pass
                elif warehouse[y+1][x] == 'O':
                    for oy in range(y+1, len(warehouse)):
                        if warehouse[oy][x] == '.':
                            for sy in range(oy, y, -1):
                                warehouse[sy][x],warehouse[sy-1][x] = warehouse[sy-1][x],warehouse[sy][x]
                            y += 1
                            break
                        elif warehouse[oy][x] == '#':
                            break
                        elif warehouse[oy][x] == 'O':
                            pass

            if move == '>':
                if warehouse[y][x+1] == '.':
                    x += 1
                    warehouse[y][x],warehouse[y][x-1] = warehouse[y][x-1],warehouse[y][x]
                elif warehouse[y][x+1] == '#':
                    pass
                elif warehouse[y][x+1] == 'O':
                    for ox in range(x+1, len(warehouse)):
                        if warehouse[y][ox] == '.':
                            for sx in range(ox, x, -1):
                                warehouse[y][sx],warehouse[y][sx-1] = warehouse[y][sx-1],warehouse[y][sx]
                            x += 1
                            break
                        elif warehouse[y][ox] == '#':
                            break
                        elif warehouse[y][ox] == 'O':
                            pass

            if move == '<':
                if warehouse[y][x-1] == '.':
                    x -= 1
                    warehouse[y][x],warehouse[y][x+1] = warehouse[y][x+1],warehouse[y][x]
                elif warehouse[y][x-1] == '#':
                    pass
                elif warehouse[y][x-1] == 'O':
                    for ox in range(x-1, 0, -1):
                        if warehouse[y][ox] == '.':
                            for sx in range(ox, x, 1):
                                warehouse[y][sx],warehouse[y][sx+1] = warehouse[y][sx+1],warehouse[y][sx]
                            x -= 1
                            break
                        elif warehouse[y][ox] == '#':
                            break
                        elif warehouse[y][ox] == 'O':
                            pass

            if move == '^':
                if warehouse[y-1][x] == '.':
                    y -= 1
                    warehouse[y][x],warehouse[y+1][x] = warehouse[y+1][x],warehouse[y][x]
                elif warehouse[y-1][x] == '#':
                    pass
                elif warehouse[y-1][x] == 'O':
                    for oy in range(y-1, 0, -1):
                        if warehouse[oy][x] == '.':
                            for sy in range(oy, y, 1):
                                warehouse[sy][x],warehouse[sy+1][x] = warehouse[sy+1][x],warehouse[sy][x]
                            y -= 1
                            break
                        elif warehouse[oy][x] == '#':
                            break
                        elif warehouse[oy][x] == 'O':
                            pass
        
        part1 = 0
        for j, row in enumerate(warehouse):
            for i, c in enumerate(row):
                if c == 'O':
                    part1 += 100*j+i

        for row in warehouse:
            print(''.join(row))

        print('Part 1', part1)

        # print(warehouse)
        # print(moves)
