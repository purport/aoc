from sys import argv

def compiled(A, program = []):
    output = []
    while A != 0:
        B = (((A & 0b111) ^ 0b101) ^ 0b110) ^ (A >> ((A & 0b111) ^ 0b101))
        A = A >> 3
        output.append(B & 0b111)

        if len(program) > 0:
            if output[-1] != program[len(output)-1]:
                return []

    return output

      #  0: B = A & 0b111
      #  2: B = B xor 0b101
      #  4: C = A shr B
      #  6: B = B xor 0b110
      #  8: A = A shr 3
      # 10: B = B ^ C
      # 12: output B & 0b111
      # 14: bnz 0

def listing_combo(operand):
    match operand:
        case 0:
            return str(operand)
        case 1:
            return str(operand)
        case 2:
            return str(operand)
        case 3:
            return str(operand)
        case 4:
            return 'A'
        case 5:
            return 'B'
        case 6:
            return 'C'
        case 7:
            return X

def combo(operand, A, B, C):
    match operand:
        case 0:
            return operand
        case 1:
            return operand
        case 2:
            return operand
        case 3:
            return operand
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7:
            raise "Illegal instruction"

def run(program, registers):
    ip = 0
    output = []
    A,B,C = registers
    while ip < len(program):
        operand = program[ip+1]
        match program[ip]:
            case 0:
                A = A//(2**combo(operand, A, B, C))
            case 1:
                B = B ^ operand
            case 2:
                B = combo(operand, A, B, C) & 0b111
            case 3:
                if A != 0 and ip != operand: ip = operand-2
            case 4:
                B = B ^ C
            case 5:
                output.append(combo(operand, A, B, C) & 0b111)
            case 6:
                B = A//(2**combo(operand, A, B, C))
            case 7:
                C = A//(2**combo(operand, A, B, C))
        ip += 2
    return output

def listing(program):
    ip = 0
    while ip < len(program):
        operand = program[ip+1]
        match program[ip]:
            case 0:
                print("%s: A = A shr %s" % ("{0:8d}".format(ip),listing_combo(operand)))
                # A = A//(2**combo(operand, A, B, C))
            case 1:
                print("%s: B = B xor 0b%s" % ("{0:8d}".format(ip),"{0:b}".format(operand)))
                # B = B ^ operand
            case 2:
                print("%s: B = %s & 0b111" % ("{0:8d}".format(ip),listing_combo(operand)))
                # B = combo(operand, A, B, C) & 0b111
            case 3:
                print("%s: bnz %s" % ("{0:8d}".format(ip),str(operand)))
                # if A != 0 and ip != operand: ip = operand-2
            case 4:
                print("%s: B = B ^ C"% ("{0:8d}".format(ip)))
                # B = B ^ C
            case 5:
                print("%s: output %s & 0b111" % ("{0:8d}".format(ip),listing_combo(operand)))
                # output.append(combo(operand, A, B, C) & 0b111)
            case 6:
                print("%s: B = A shr %s" % ("{0:8d}".format(ip),listing_combo(operand)))
                # B = A//(2**combo(operand, A, B, C))
            case 7:
                print("%s: C = A shr %s" % ("{0:8d}".format(ip),listing_combo(operand)))
                # C = A//(2**combo(operand, A, B, C))
        ip += 2


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        registers = []
        program = ""
        for index, line in enumerate(file):
            if index < 3:
                registers.append(int(line.split()[-1]))
            if index == 4:
                program = [int(x.strip()) for x in line.split()[-1].split(',')]

        output = run(program, registers)
        print('Part 1', ','.join([str(x) for x in output]))
        print('Part 1', ','.join([str(x) for x in compiled(registers[0])]))


        A = int(0) 
        for index in range(len(program)-1,-1,-1):
            found = False
            for digit in range(8):
                quine = run(program, [A | (digit<<(3*index)),0,0])
                if index < len(quine) and quine[index] == program[index]:
                    A = A | (digit << (3*index))
                    found = True
                    break
            if not found:
                print("Not found")


        print('Part 2', A)
        binA = "{0:048b}".format(A)
        print('Part 2', "_".join([binA[i:i+3] for i in range(0, len(binA), 3)]))
        print('Part 2', ','.join([str(x) for x in run(program, [A, 0, 0])]))
        print('Part 2', ','.join([str(x) for x in program]))

        # A = 0b011_000_000_110_011_000_011_011_110_111_000_011_010_111_010_010

        print()
        i = 3 
        A = 105690555219968 
        A = 105716325023744
        A = 105839805333504
        A = 105840476422144
        A = 105840577085440
        A = 105843716521984
        A = 105843716587520
        A = 105843716612096
        A = 105843716614144
        A = 105843716614528
        A = 105843716614552

        A = A & ~(0b111 << (3*i))
        A = A & ~(0b111 << (3*(i-1)))
        A = A & ~(0b111 << (3*(i-2)))
        A = A & ~(0b111 << (3*(i-3)))
        for digit1 in range(8):
            for digit2 in range(8):
                for digit3 in range(8):
                    for digit4 in range(8):
                        newA = A | (digit1<<(3*i))
                        newA = newA | (digit2<<(3*(i-1)))
                        newA = newA | (digit3<<(3*(i-2)))
                        newA = newA | (digit4<<(3*(i-3)))
                        # print(digit1, digit2)
                        # binA = "{0:048b}".format(newA)
                        # print('Part 2', "_".join([binA[i:i+3] for i in range(0, len(binA), 3)]))
                        quine = run(program, [newA,0,0])
                        if i >= len(quine): continue
                        if quine[i] == program[i] and quine[i-1] == program[i-1] and quine[i-2] == program[i-2] and quine[i-3] == program[i-3]:
                            print(digit4, digit3, digit2, digit1)
                            print(newA)
                            print('Part 2', ','.join([str(x) for x in quine]), digit1)
                            print('Actual', ','.join([str(x) for x in program]))
                            print()
                            exit(0)
        listing(program)

        # print('Part 2', A)

