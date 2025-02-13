if __name__ == '__main__':
    with open('popular-names.txt', 'r', encoding='ascii') as f:
        lines = f.readlines()
        freq = {}
        for index, line in enumerate(lines):
            spl = line.strip().split('\t')
            name = spl[0]
            freq[name] = freq.get(name, 0) + 1
        l = [(-f, k) for k, f in freq.items()]
        l.sort()
        for entry in l:
            print(f'{-entry[0]: 4d} {entry[1]}')
