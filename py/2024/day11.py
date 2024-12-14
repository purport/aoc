from sys import argv


cache = {}
def blinks(stone, i, n):
    key = (stone, i, n)
    if key in cache: return cache[key]
    count = 1
    for blink in range(i, n):
        if stone == 0:
            stone = 1
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            count += blinks(int(s[:len(s)//2]), blink+1, n) + blinks(int(s[len(s)//2:]), blink+1, n)-1
            break
        else:
            stone *= 2024

    cache[key] = count
    return count


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        stones = [[int(ch) for ch in line.split(' ')] for line in file][0]
        print(stones)
        part1 = 0
        part2 = 0
        for stone in stones:
            part1 += blinks(stone, 0, 25)
            part2 += blinks(stone, 0, 75)
        print('Part 1', part1)
        print('Part 2', part2)

        #
        #
        # for blink in range(0, 25):
        #     new_stones = []
        #     for stone in stones:
        #         if stone == 0:
        #             new_stones.append(1)
        #         elif len(str(stone)) % 2 == 0:
        #             s = str(stone)
        #             new_stones+=[int(s[:len(s)//2]), int(s[len(s)//2:])]
        #         else:
        #             new_stones.append(stone*2024)
        #     stones = new_stones
        #     print('Done blink', blink)
        # # print(stones)
        # print('Part 1', len(stones))
