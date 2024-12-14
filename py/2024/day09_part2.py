from sys import argv


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        blocks = [[int(ch) for ch in line.split()[0]] for line in file][0]
        disk = []
        index = 0
        for i, block in enumerate(blocks):
            if i % 2 == 0:
                disk.append([index]*block)
                index += 1
            else:
                disk.append(['.']*block)

        pre = [','.join([str(x) for x in block]) for block in disk]

        new_block = []
        free_block = 1
        free_length = len(disk[free_block])
        used_block = len(disk)
        used_block -= 1
        while free_block < used_block:
            while len(disk[used_block]) == 0:
                used_block -= 2
            if free_length == 0:
                disk[free_block] = new_block
                new_block = []
                free_block += 2
                free_length = len(disk[free_block])

            if free_length != 0:
                new_block.append(disk[used_block].pop())
                free_length -= 1

        if len(new_block) > 0:
            disk[used_block].append(*new_block)
            
        post = [','.join([str(x) for x in block]) for block in disk]
        print("\n".join(["{:40s}  -  {:40s}".format(x,y) for x, y in zip(pre, post)]))
        index = 0
        part2 = 0
        for block in disk:
            for file in block:
                if file != '.':
                    part2 += file*index
                    index += 1

        print("Part 2", part2)

