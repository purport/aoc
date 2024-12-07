from sys import argv


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        equations = [[int(s.strip(':')) for s in line.split()] for line in file]
        part1 = 0
        for result, *args in equations:
            comb = [0 for _ in range(len(args)-1)]
            combi = 0
            for mask in range(3**(len(args)-1)):
                calc = args[0]
                formula = [calc]
                for i, arg in enumerate(args[1::]):
                    match comb[i]:
                        case 0:
                            formula.append('*')
                            formula.append(arg)
                            calc *= arg
                        case 1:
                            formula.append('+')
                            formula.append(arg)
                            calc += arg
                        case 2:
                            formula.append('||')
                            formula.append(arg)
                            calc = int(str(calc) + str(arg))
                    if calc > result: break
                if calc == result:
                    part1 += result
                    break
                while combi < len(comb):
                    comb[combi] += 1
                    if comb[combi] == 3:
                        comb[combi] = 0
                        combi += 1
                    else:
                        combi = 0
                        break
        print('Part 1', part1)





