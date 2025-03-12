import importlib
m30 = importlib.import_module("30")

if __name__ == '__main__':
    # 形態素解析の実行
    neko_morphemes = m30.analyze_neko()

    # 表層形（surface）のみを列挙
    surfaces = [morpheme['surface'] for morpheme in neko_morphemes if morpheme['pos'] == '動詞']

    # 結果の表示（最初の20個）
    print('表層形の列挙（最初の20個）:')
    for i, surface in enumerate(surfaces[:20]):
        print(f"{i+1}: {surface}")

    # 表層形の総数を表示
    print(f"\n表層形の総数: {len(surfaces)}")
