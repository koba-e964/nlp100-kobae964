import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    with open('popular-names.txt', 'r', encoding='ascii') as f:
        lines = f.readlines()
        for line in lines[:n]:  # Error handling omitted
            print(line, end='')
