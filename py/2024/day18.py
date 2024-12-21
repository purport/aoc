from sys import argv

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        corruptions = [[int(s) for s in line.split(',')] for line in file]
        maze = [['.' for _ in range(71)] for _ in range(71)]
        for i in range(1024):
            col,row = corruptions[i]
            maze[row][col] = '#'

        u = 0,0
        e = (70,70)
        P = {}
        T = {}
        P[u] = 0
        while u != e:
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                x = col, row = u[0]+dx,u[1]+dy
                if x in P: continue
                if 0 <= row <= 70 and 0 <= col <= 70:
                    if maze[row][col] == '#': continue
                    if x not in T or (P[u] + 1 < T[x]):
                        T[x] = P[u] + 1
            
            cost = -1
            for x in T:
                if T[x] < cost or cost == -1:
                    cost = T[x]
                    u = x
            if cost < 0: 
                print("Error...")
                break
            P[u] = cost
            del T[u]


        print('Part 1', P[u])

        index=0
        while u != (0,0):
            index += 1
            col,row = u
            if maze[row][col] == '.':
                maze[row][col] = 'O'
            
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                x = col+dx,row+dy
                if x not in P: continue
                if P[x] + 1 == P[u]:
                    u = x
        maze[0][0] = 'O'

        for i in range(len(corruptions)):
            col,row = corruptions[i]
            # if maze[row][col] == 'O':
            maze[row][col] = '#'
            u = 0,0
            e = (70,70)
            P = {}
            T = {}
            P[u] = 0
            while u != e:
                for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                    x = col, row = u[0]+dx,u[1]+dy
                    if x in P: continue
                    if 0 <= row <= 70 and 0 <= col <= 70:
                        if maze[row][col] == '#': continue
                        if x not in T or (P[u] + 1 < T[x]):
                            T[x] = P[u] + 1
                
                cost = -1
                for x in T:
                    if T[x] < cost or cost == -1:
                        cost = T[x]
                        u = x
                if cost < 0: 
                    break
                P[u] = cost
                del T[u]

            if u != e:
                print('Part 2',i,  col,row)
                break

        # for row in maze:
        #     print(''.join(row))
