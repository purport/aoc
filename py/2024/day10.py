from sys import argv

d = [(1,0),(-1,0),(0,1),(0,-1)]
def traverse(heads, g, i, j):
    if g[j][i] == 9: 
        if heads[j][i] == 1: return 0
        heads[j][i] = 1
        return 1
    count = 0
    for (di,dj) in d:
        next_i = i+di
        next_j = j+dj
        if not 0 <= next_j < len(g): continue 
        if not 0 <= next_i < len(g[0]): continue 
        if g[j][i] + 1 == g[next_j][next_i]:
            count += traverse(heads, g, next_i, next_j)
    return count

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        g = [[99 if ch == '.' else int(ch) for ch in line.split()[0]] for line in file]
        heads = [[0 for n in line] for line in g]
        zeros = []
        for j, row in enumerate(g):
            zeros += [(i,j) for i,x in enumerate(row) if x == 0]

        part1 = 0
        for i,j in zeros:
            heads = [[0 for n in line] for line in g]
            count = traverse(heads, g, i,j)
            part1 += count
            
        print('Part 1', part1)
