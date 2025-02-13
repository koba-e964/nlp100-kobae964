if __name__ == '__main__':
    with open('popular-names.txt', 'r', encoding='ascii') as f:
        lines = f.readlines()
        for line in lines:
            print(line.replace('\t', ' '), end='')
