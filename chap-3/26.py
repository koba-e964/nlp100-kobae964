import importlib
import json
m25 = importlib.import_module("25")


def extract_country_info(filename: str) -> dict[str, str]:
    dat = m25.extract_country_info(filename)
    converted = {}
    for k, v in dat.items():
        converted[k] = v.replace("'''''", "").replace("'''", "").replace("''", "")
    return converted


if __name__ == '__main__':
    dat = extract_country_info('uk.txt')
    print(json.dumps(dat))
