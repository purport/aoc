from sys import argv

def path(maze, s, e):
    P = {}
    T = {}
    u = s
    P[u] = 0
    while u != e:
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            x = row,col = u[0]+dy,u[1]+dx
            if not (0 <= row < len(maze) and 0 <= col < len(maze[0])): continue
            if maze[row][col] == '#': continue
            if x in P: continue
            if x not in T or P[u] + 1 < T[x]:
                T[x] = P[u]+1

        cost = -1
        for x in T:
            if cost == -1 or cost > T[x]:
                cost = T[x]
                u = x
        P[u] = cost
        del T[u]

        if cost == -1: break

    return P

def minpath(s, e, P):
    u = e
    path = []
    while u != s:
        path.append(u)
        found = False
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            x = row,col = u[0]+dy,u[1]+dx
            if x in P and P[x] + 1 == P[u]:
                u = x
                found = True
                break
        if not found: return []
    path.append(s)
    return path


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        maze = [[b for b in line.strip()] for line in file]
        rows = len(maze)
        cols = len(maze[0])
        s = (0,0)
        e = (0,0)
        for row in range(rows):
            for col in range(cols):
                if 'S' == maze[row][col]:
                    s = (row,col)
                if 'E' == maze[row][col]:
                    e = (row,col)

        P = path(maze, s, e)
        p = minpath(s, e, P)
        # print(P[e])
        for i,u in enumerate(p):
            row,col = u
            maze[row][col] = 'O' # P[u]

        part1 = 0
        savings = {}
        for i,u in enumerate(p):
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                row,col = u[0]+dy,u[1]+dx
                if maze[row][col] == '#':
                    x = row+dy, col+dx
                    if x in P:
                        saving = P[x] - P[u] - 2
                        if saving >= 100:
                            part1 += 1
                            if saving not in savings: savings[saving] = 0
                            savings[saving] += 1

        
        print("Part 1", part1)



