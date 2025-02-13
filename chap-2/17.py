if __name__ == '__main__':
    with open('popular-names.txt', 'r', encoding='ascii') as f:
        lines = f.readlines()
        s = set()
        for line in lines:
            spl = line.strip().split('\t')
            s.add(spl[0])
        l = list(s)
        l.sort()
        for entry in l:
            print(entry)
