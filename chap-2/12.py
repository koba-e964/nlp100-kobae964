if __name__ == '__main__':
    with open('popular-names.txt', 'r', encoding='ascii') as f:
        with open('col1.txt', 'w', encoding='ascii') as col1:
            with open('col2.txt', 'w', encoding='ascii') as col2:
                lines = f.readlines()
                for line in lines:
                    splitted = line.strip().split('\t')
                    col1.write(splitted[0] + '\n')
                    col2.write(splitted[1] + '\n')
