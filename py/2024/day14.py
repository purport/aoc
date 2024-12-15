from sys import argv
import os

if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        robots = [[y for s in line.split() for i, y in enumerate(s.split('=')) if i % 2 == 1] for line in file]
        positions = []
        velocities = []
        for position, velocity in robots:
            px,py = [int(p) for p in position.split(',')]
            vx,vy = [int(v) for v in velocity.split(',')]
            positions.append((px,py))
            velocities.append((vx,vy))
        tilex = 101
        tiley = 103 
        for time in range(100000):
            bathroom = [[0 for _ in range(tilex)] for _ in range(tiley)]
            for (px,py), (vx,vy) in zip(positions,velocities):
                tx = (px + vx*time)%tilex
                ty = (py + vy*time)%tiley
                bathroom[ty][tx] += 1

            
            longest = 0
            for row in bathroom:
                start = -1
                for i, t in enumerate(row):
                    if t != 0 and start == -1: start = i
                    if start != -1 and t == 0:
                        longest = max(i-start,longest)
                        start = -1

            if longest > 30:
                os.system('clear')
                print("Time = ", time)
                for row in bathroom:
                    print(''.join([' ' if x == 0 else '#' for x in row]))
                print()
                print()
                print()
                print()
            # q1 = 0
            # q2 = 0
            # q3 = 0
            # q4 = 0
            # for x in range(0, (tilex-1)//2):
            #     for y in range(0, (tiley-1)//2):
            #         q1 += bathroom[y][x]
            # for x in range((tilex-1)//2+1, tilex):
            #     for y in range(0, (tiley-1)//2):
            #         q2 += bathroom[y][x]
            # for x in range((tilex-1)//2+1, tilex):
            #     for y in range((tiley-1)//2+1, tiley):
            #         q3 += bathroom[y][x]
            # for x in range(0, (tilex-1)//2):
            #     for y in range((tiley-1)//2+1, tiley):
            #         q4 += bathroom[y][x]

        # print(q1, q2, q3, q4)
        # print('Part 1', q1*q2*q3*q4)

