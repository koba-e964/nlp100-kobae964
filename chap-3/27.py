import importlib
import json
import re
m26 = importlib.import_module("26")


pat0 = re.compile(r'\[\[[^\]]+\|([^\]]+)\]\]')
pat1 = re.compile(r'\[\[([^\]]+)\]\]')

def extract_country_info(filename: str) -> dict[str, str]:
    dat = m26.extract_country_info(filename)
    converted = {}
    for k, v in dat.items():
        converted[k] = pat0.sub(r'\1', v)
        converted[k] = pat1.sub(r'\1', converted[k])
    return converted


if __name__ == '__main__':
    dat = extract_country_info('uk.txt')
    print(json.dumps(dat))
