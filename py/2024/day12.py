from sys import argv
import copy

# *------*
# |00000 | 
# | *----*
# |0|1111| 
# | *----*
# |00000 | 
# | *----*
# |0|2222| 
# | *----*
# |00000 |
# *------*

# 4 = e - 12 + 2

# down, up, right, left

d = [(1,0),(0,-1),(-1,0),(0,1)]
def fill(regions, areas, perimeters, index, i, j):
    if type(areas[j][i]) is not str: return False
    region = regions[j][i]
    areas[j][i] = index 
    perimeter = 4
    
    for (di,dj) in d:
        next_i = i+di
        next_j = j+dj
        if not 0 <= next_j < len(regions): continue 
        if not 0 <= next_i < len(regions[0]): continue 
        if regions[next_j][next_i] == region:
            perimeter -= 1

        if type(areas[next_j][next_i]) is not str: continue
        if regions[next_j][next_i] == region:
            fill(regions, areas, perimeters, index, next_i, next_j)

    perimeters[j][i] = perimeter
    return True

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        regions = [[ch for ch in line.split()[0]] for line in file]
        areas = copy.deepcopy(regions)
        perimeters = copy.deepcopy(regions)
        count = 0 
        for j, line in enumerate(regions):
            for i, x in enumerate(line):
                if type(x) is not str: continue
                if fill(regions,areas,perimeters,count,i,j):
                    count += 1

        total_area = {}
        total_perimeter = {}
        corners = copy.deepcopy(areas)
        for j, line in enumerate(areas):
            for i, x in enumerate(line):
                total_area[x] = total_area.get(x, 0)
                total_area[x] = total_area[x]+1
                total_perimeter[x] = total_perimeter.get(x, 0)
                total_perimeter[x] = total_perimeter[x]+perimeters[j][i]
                
                c = [[0,0,0],[0,0,0],[0,0,0]]
                for dj in range(-1, 2):
                    for di in range(-1, 2):
                        next_i = i+di
                        next_j = j+dj
                        if not 0 <= next_j < len(areas): continue 
                        if not 0 <= next_i < len(areas[0]): continue 
                        print(next_i,next_j,areas[next_j][next_i])
                        c[dj][di] = 1 if areas[next_j][next_i] == areas[j][i] else 0

                print("\n".join(["".join([str(y) for y in x]) for x in c]))
                print()


        print("\n".join([str(c) for c in corners]))
        print()

        print(total_area)
        print(total_perimeter)
        part1 = 0
        edges = 0
        vertices =16 
        for index in range(0, count):
            part1 += total_area[index]*total_perimeter[index]
            edges += total_perimeter[index]
            vertices += total_area[index]

            
        print('Part 1', part1)
