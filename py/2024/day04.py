from sys import argv

def search(grid, x, y, dx, dy, ch = 'X'):
    if 0<= y<len(grid) and 0<=x<len(grid[0]) and grid[y][x] == ch:
        match ch:
            case 'X': ch = 'M'
            case 'M': ch = 'A'
            case 'A': ch = 'S'
            case 'S': return 1
        return search(grid, x+dx,y+dy, dx,dy,ch)
    return 0

def search2(grid, x, y):
    if 0< y<len(grid)-1 and 0<x<len(grid[0])-1 and grid[y][x] == 'A':
        if grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'S':
            if grid[y+1][x-1] == 'M' and grid[y+1][x+1] == 'S':
                return 1
        if grid[y-1][x-1] == 'S' and grid[y-1][x+1] == 'M':
            if grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'M':
                return 1
        if grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'M':
            if grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'S':
                return 1
        if grid[y-1][x-1] == 'S' and grid[y-1][x+1] == 'S':
            if grid[y+1][x-1] == 'M' and grid[y+1][x+1] == 'M':
                return 1
    return 0

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        grid = [line.strip() for line in file]
        part1 = 0;
        part2 = 0;
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                part2 += search2(grid, x,y)
                part1 += search(grid,x,y, 0, 1)
                part1 += search(grid,x,y, 1, 1)
                part1 += search(grid,x,y, 1, 0)
                part1 += search(grid,x,y, 1, -1)
                part1 += search(grid,x,y, -1, 1)
                part1 += search(grid,x,y, -1, 0)
                part1 += search(grid,x,y, -1, -1)
                part1 += search(grid,x,y, 0, -1)
        print('Part 1', part1)
        print('Part 2', part2)
