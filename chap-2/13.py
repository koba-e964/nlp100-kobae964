if __name__ == '__main__':
    with open('col1.txt', 'r', encoding='ascii') as col1:
        with open('col2.txt', 'r', encoding='ascii') as col2:
            with open('merged.txt', 'w', encoding='ascii') as merged:
                col1_lines = col1.readlines()
                col2_lines = col2.readlines()
                for i in range(len(col1_lines)):
                    merged.write(col1_lines[i].strip() + '\t' + col2_lines[i].strip() + '\n')
