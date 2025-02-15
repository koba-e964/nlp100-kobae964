import re
import json

pat = re.compile(r'^==.*==$')

if __name__ == '__main__':
    dat = []
    with open('uk.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            match = pat.match(line)
            if match:
                level = 0
                while line.startswith('=') and line.endswith('='):
                    level += 1
                    line = line[1:len(line) - 1]
                dat.append({'level': level - 1, 'name': line})
    print(json.dumps(dat))
