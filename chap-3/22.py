import re

pat = re.compile(r'\[\[Category:([^\|]*).*\]\]')

if __name__ == '__main__':
    with open('uk.txt', 'r', encoding='utf-8') as f:
        for line in f:
            match = pat.match(line)
            if match:
                print(match[1])
