from sys import argv

def rotate(drow, dcol):
    match (drow,dcol):
        case (-1,0):
            return (0,1)
        case (0,1):
            return (1,0)
        case (1,0):
            return (0,-1)
        case (0,-1):
            return (-1,0)

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        grid = [line.strip() for line in file]
        row = 0
        col = 0
        for y, line in enumerate(grid):
            x = line.find("^")
            if x >= 0:
                row = y
                col = x
                break

        part1 = 1
        part2 = 0
        drow = -1
        dcol = 0
        up = 0
        down = 0
        left = 0
        right = 0
        step = 0
        while row != 0 and col != 0 and row != len(grid)-1 and col != len(grid[0])-1:
            while grid[row+drow][col+dcol] == '#':
                drow,dcol = rotate(drow,dcol)
                if drow > 0: down = 0
                if drow < 0: up = 0
                if dcol > 0: right = 0
                if dcol < 0: left = 0
                line = grid[row]
                grid[row] = line[:col] + '@' + line[col+1:]

            row += drow
            col += dcol

            if grid[row][col] != ' ':
                line = grid[row]
                grid[row] = line[:col] + ' ' + line[col+1:]
                part1 += 1

            if up == down and left == right and left > 0 and right > 0:
                line = grid[row]
                grid[row] = line[:col] + '*' + line[col+1:]
                print('hello')
                break;

            if drow < 0: up += 1
            if drow > 0: down += 1
            if dcol < 0: left += 1
            if dcol > 0: right += 1



            step += 1
            # if step == 190:
            #     break

        for line in grid:
            print(line)
        print("Part 1", part1)
        print("Part 2", part2)
