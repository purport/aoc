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
            row2 = []
            for c in row:
                match c:
                    case '.': row2 += ['.','.']
                    case '#': row2 += ['#','#']
                    case '@': row2 += ['@','.']
                    case 'O': row2 += ['[',']']
            if '@' in row2:
                x = row2.index('@')
            if x == 0: y += 1
            warehouse.append(row2)
        moves = ''
        for line in file:
            moves += line.strip()

        for index, move in enumerate(moves):
            # print(index, 'move', move)
            if move == 'v':
                if warehouse[y+1][x] == '.':
                    y += 1
                    warehouse[y][x],warehouse[y-1][x] = warehouse[y-1][x],warehouse[y][x]
                elif warehouse[y+1][x] == '[' or warehouse[y+1][x] == ']':
                    check = []
                    moves = []
                    if warehouse[y+1][x] == '[':
                        check += [(x,y+2),(x+1,y+2)]
                        moves += [(x,y+1),(x+1,y+1)]
                    if warehouse[y+1][x] == ']':
                        check += [(x,y+2),(x-1,y+2)]
                        moves += [(x,y+1),(x-1,y+1)]

                    blocked = False
                    while len(check) != 0:
                        nx,ny = check[0]
                        del check[0]
                        if warehouse[ny][nx] == '#':
                            blocked = True
                            break
                        elif warehouse[ny][nx] == '[':
                            check += [(nx,ny+1),(nx+1,ny+1)]
                            if (nx,ny) not in moves:
                                moves.append((nx,ny))
                            if (nx+1,ny) not in moves:
                                moves.append((nx+1,ny))
                        elif warehouse[ny][nx] == ']':
                            check += [(nx,ny+1),(nx-1,ny+1)]
                            if (nx,ny) not in moves:
                                moves.append((nx,ny))
                            if (nx-1,ny) not in moves:
                                moves.append((nx-1,ny))

                    # if index == 309: print(moves)
                    if len(check) == 0 and not blocked:
                        while len(moves) != 0:
                            nx,ny = moves.pop()
                            warehouse[ny+1][nx],warehouse[ny][nx] = warehouse[ny][nx],warehouse[ny+1][nx]
                        y += 1
                        warehouse[y-1][x],warehouse[y][x] = warehouse[y][x],warehouse[y-1][x]
            if move == '^':
                if warehouse[y-1][x] == '.':
                    y -= 1
                    warehouse[y][x],warehouse[y+1][x] = warehouse[y+1][x],warehouse[y][x]
                elif warehouse[y-1][x] == '[' or warehouse[y-1][x] == ']':
                    check = []
                    moves = []
                    if warehouse[y-1][x] == '[':
                        check += [(x,y-2),(x+1,y-2)]
                        moves += [(x,y-1),(x+1,y-1)]
                    if warehouse[y-1][x] == ']':
                        check += [(x,y-2),(x-1,y-2)]
                        moves += [(x,y-1),(x-1,y-1)]

                    blocked = False
                    while len(check) != 0:
                        nx,ny = check[0]
                        del check[0]
                        # print((nx,ny), check)
                        if warehouse[ny][nx] == '#':
                            blocked = True
                            break
                        elif warehouse[ny][nx] == '[':
                            check += [(nx,ny-1),(nx+1,ny-1)]
                            if (nx,ny) not in moves:
                                moves.append((nx,ny))
                            if (nx+1,ny) not in moves:
                                moves.append((nx+1,ny))
                        elif warehouse[ny][nx] == ']':
                            check += [(nx,ny-1),(nx-1,ny-1)]
                            if (nx,ny) not in moves:
                                moves.append((nx,ny))
                            if (nx-1,ny) not in moves:
                                moves.append((nx-1,ny))

                    # if index == 21: print(moves)
                    if len(check) == 0 and not blocked:
                        while len(moves) != 0:
                            nx,ny = moves.pop()
                            warehouse[ny-1][nx],warehouse[ny][nx] = warehouse[ny][nx],warehouse[ny-1][nx]
                        y -= 1
                        warehouse[y+1][x],warehouse[y][x] = warehouse[y][x],warehouse[y+1][x]
            if move == '<':
                if warehouse[y][x-1] == '.':
                    x -= 1
                    warehouse[y][x],warehouse[y][x+1] = warehouse[y][x+1],warehouse[y][x]
                elif warehouse[y][x-1] == ']':
                    for ox in range(x-3, 0, -1):
                        if warehouse[y][ox] == '.':
                            for sx in range(ox, x, 1):
                                warehouse[y][sx],warehouse[y][sx+1] = warehouse[y][sx+1],warehouse[y][sx]
                            x -= 1
                            break
                        elif warehouse[y][ox] == '#':
                            break
            if move == '>':
                if warehouse[y][x+1] == '.':
                    x += 1
                    warehouse[y][x],warehouse[y][x-1] = warehouse[y][x-1],warehouse[y][x]
                elif warehouse[y][x+1] == '[':
                    for ox in range(x+3, len(warehouse[0])):
                        # print(ox, warehouse[y][ox])
                        if warehouse[y][ox] == '.':
                            for sx in range(ox, x, -1):
                                warehouse[y][sx],warehouse[y][sx-1] = warehouse[y][sx-1],warehouse[y][sx]
                            x += 1
                            break
                        elif warehouse[y][ox] == '#':
                            break

            # print(index, 'Move', move)
            # for row in warehouse:
            #     print(''.join(row))
            # print()
            # if index == 35:
            #     break

        
        part1 = 0
        for j, row in enumerate(warehouse):
            for i, c in enumerate(row):
                if c == '[':
                    part1 += 100*j + i

        for row in warehouse:
            print(''.join(row))

        print('Part 1', part1)

        # print(warehouse)
        # print(moves)
