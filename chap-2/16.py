import sys

if __name__ == '__main__':
    n = int(sys.argv[1])
    with open('popular-names.txt', 'r', encoding='ascii') as f:
        lines = f.readlines()
    for i in range(n):
        with open(f'16-{i}.txt', 'w', encoding='ascii') as f:
            for j in range(len(lines)*i//n, len(lines)*(i+1)//n):
                f.write(lines[j])
