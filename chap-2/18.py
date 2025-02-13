if __name__ == '__main__':
    with open('popular-names.txt', 'r', encoding='ascii') as f:
        lines = f.readlines()
        sorter = []
        for index, line in enumerate(lines):
            spl = line.strip().split('\t')
            sorter.append((int(spl[2]), -index, line))
        sorter.sort(reverse=True)
        for entry in sorter:
            print(entry[2], end='')
