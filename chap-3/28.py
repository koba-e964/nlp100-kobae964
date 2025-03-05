import importlib
import json
import re
m27 = importlib.import_module("27")


pat_ref0 = re.compile(r'<ref name=\"[^>]+\" />')
pat_ref1 = re.compile(r'<ref[^/]*>.+</ref>')


def extract_country_info(filename: str) -> dict[str, str]:
    dat = m27.extract_country_info(filename)
    converted = {}
    for k, v in dat.items():
        tmp = pat_ref0.sub('', v)
        converted[k] = pat_ref1.sub('', tmp)
    return converted


if __name__ == '__main__':
    dat = extract_country_info('uk.txt')
    print(json.dumps(dat))
