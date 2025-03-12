import importlib
m30 = importlib.import_module("30")

if __name__ == '__main__':
    neko_morphemes = m30.analyze_neko()
    bases = [morpheme['base'] for morpheme in neko_morphemes if morpheme['pos'] == '動詞']

    print('基本形の列挙（最初の20個）:')
    for i, surface in enumerate(bases[:20]):
        print(f"{i+1}: {surface}")

    print(f"\n基本形の総数: {len(bases)}")
