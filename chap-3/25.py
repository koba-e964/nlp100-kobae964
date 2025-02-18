import re
import json

pat = re.compile(r'\{\{基礎情報 国.*(|.*\n)*.*\}\}', re.MULTILINE)
entry = re.compile(r'\|([^=]+)=(.+)\n', re.MULTILINE)


def extract_country_info(filename: str) -> dict[str, str]:
    dat = {}
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        ma = pat.search(content, re.MULTILINE)
        index = ma.start() + 1 # the first '{'
        level = 1
        pos = index
        while level > 0:
            if content[pos] == '{':
                level += 1
            elif content[pos] == '}':
                level -= 1
            pos += 1
        last_bar = None
        split: list[str] = []
        for i in range(index - 1, pos):
            if content[i] == '{':
                level += 1
            elif content[i] == '}':
                level -= 1
            if level == 2 and content[i] == '|':
                if last_bar is not None:
                    split.append(content[last_bar + 1:i])
                last_bar = i
        for s in split:
            ind = s.find('=')
            if ind != -1:
                key = s[:ind].strip()
                val = s[ind + 1:].strip()
                dat[key] = val
    return dat


if __name__ == '__main__':
    dat = extract_country_info('uk.txt')
    print(json.dumps(dat))
