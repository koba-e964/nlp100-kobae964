import json


if __name__ == '__main__':
    with open('jawiki-country.json', 'r', encoding='utf-8') as f:
        for line in f:
            entry = json.loads(line)
            if entry['title'] == 'イギリス':
                with open('uk.txt', 'w', encoding='utf-8') as f:
                    f.write(entry['text'])
                break

