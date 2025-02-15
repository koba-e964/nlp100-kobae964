if __name__ == '__main__':
    with open('uk.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('[[Category:'):
                print(line.strip())
