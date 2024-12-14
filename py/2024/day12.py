from sys import argv


if __name__ ==  "__main__":
    with open(argv[1], 'r') as file:
        blocks = [[int(ch) for ch in line.split()[0]] for line in file][0]
