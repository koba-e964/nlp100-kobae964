import importlib
import re
import requests
m28 = importlib.import_module("28")


pat_ref0 = re.compile(r'<ref name=\"[^>]+\" />')
pat_ref1 = re.compile(r'<ref[^/]*>.+</ref>')


def extract_national_flag(filename: str) -> None:
    dat = m28.extract_country_info(filename)
    filename = dat['国旗画像']
    url = f'https://www.mediawiki.org/w/api.php?action=query&titles=File:{filename}&prop=imageinfo&format=json&iiprop=url'
    r = requests.get(url)
    data = r.json()
    url = data["query"]["pages"]["-1"]["imageinfo"][0]["url"]
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    extract_national_flag('uk.txt')
