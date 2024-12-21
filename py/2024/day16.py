from sys import argv

def get_direction(orientation):
    match orientation%4:
        case 0: return  1, 0
        case 1: return  0,-1
        case 2: return -1, 0
        case 3: return  0, 1

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        maze = [[s for s in line.strip()] for line in file]
        ex,ey = 0,0
        sx,sy = 0,0
        for y, row in enumerate(maze):
            if 'E' in row:
                ex = row.index('E')
                ey = y
            if 'S' in row:
                sx = row.index('S')
                sy = y

        P = {}
        T = {}

        u = sx,sy,0
        P[u] = (0)
        while True:
            for d in [(1,0,0),(0,1,1),(-1,0,2),(0,-1,3)]:
                x = (u[0]+d[0], u[1]+d[1], d[2])
                if maze[x[1]][x[0]] == '#': continue
                if x in P: continue
                cost = abs(u[2] - x[2])
                if cost > 2: cost = 4-cost
                cost = cost*1000 + 1
                if x not in T or (P[u]+cost < T[x]):
                    T[x] = P[u]+cost

            cost = -1
            for x in T:
                if T[x] < cost or cost == -1:
                    cost = T[x]
                    u = x
            if cost < 0: 
                break
            P[u] = cost
            del T[u]
                
            if u[0] == ex and u[1] == ey: break

        index=0
        stack = [(u, P[u])]
        part1 = P[u]
        part2 = 2
        while len(stack) != 0:
            index += 1
            u,P_u = stack.pop()
            if maze[u[1]][u[0]] == '.':
                maze[u[1]][u[0]] = 'O'
                part2 += 1
            for d in [(-1,0),(0,-1),(1,0),(0,1)]:
                for o in range(4):
                    x = (u[0]+d[0], u[1]+d[1], o)
                    if x in P:
                        cost = abs(x[2] - u[2])
                        if cost > 2: cost = 4-cost
                        cost = cost*1000 + 1
                        if P[x] + cost == P_u:
                            stack.append((x, P[x]))

        print('Part 1', part1)
        print('Part 2', part2)
