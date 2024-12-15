from sys import argv
import sys

def pivot_column(tableau):
    return min(range(len(tableau[-1])), key=lambda i: tableau[-1][i])

def pivot_row(tableau, pivot_column):
    least_positive = 0
    pivot_row =-1 
    for i, row in enumerate(tableau[:-1]):
        if row[pivot_column] > 0:
            ratio = row[-1]/row[pivot_column]
            if (0 < ratio < least_positive) or (ratio > 0 and least_positive == 0):
                least_positive = ratio
                pivot_row = i
    return pivot_row

def solve(tableau):
    while True:
        pc = pivot_column(tableau)
        if tableau[-1][pc] >= 0: break
        pr = pivot_row(tableau, pc)
        
        multiplier = 1.0 / tableau[pr][pc]
        for i in range(len(tableau[0])):
            tableau[pr][i] *= multiplier
            
        for i, row in enumerate(tableau):
            if i == pr: continue
            m = row[pc]
            for j in range(len(row)):
                row[j] -= m * tableau[pr][j]

# tableau = [[94, 22, 1, 0, 8400],[34, 67, 0, 1, 5400],[-1, -1, 0, 0, 0]]
# solve(tableau)
# a = int(tableau[0][-1])
# b = int(tableau[1][-1])
# print(a,b)
# exit(1)

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        a = []
        b = []
        prize = []
        for i, line in enumerate(file):
            if i % 4 == 0:
                 x = int(line.split()[2].split('+')[1].strip(','))
                 y = int(line.split()[3].split('+')[1].strip(','))
                 a.append((x,y))
            if i % 4 == 1:
                 x = int(line.split()[2].split('+')[1].strip(','))
                 y = int(line.split()[3].split('+')[1].strip(','))
                 b.append((x,y))
            if i % 4 == 2:
                 x = int(line.split()[1].split('=')[1].strip(','))
                 y = int(line.split()[2].split('=')[1].strip(','))
                 prize.append((x,y))

        part1 = 0
        for [ax,ay], [bx,by], [x,y] in zip(a,b,prize):
            tableau = [[ax, bx, 1, 0, (x+10000000000000)],\
                       [ay, by, 0, 1, (y+10000000000000)],\
                       [-ax-ay+3, -bx-by+1, 0, 0, 0]]
            # for row in tableau:
            #     print(row)
            # print()
            solve(tableau)
            # for row in tableau:
            #     print(row)
            # print()
            a=0
            b=0
            for row in tableau:
                a += row[0]*row[-1]
                b += row[1]*row[-1]
            # print(a,b)
            # print(a*ax+b*bx,x)
            # print(a*ay+b*by,y)
            # print()
            # print()
            # print()
            a = round(a)
            b = round(b)
            if a*ax+b*bx == x+10000000000000 and a*ay+b*by == y+10000000000000:
                part1 += 3*a+b
                
        print('Part 1', part1)
