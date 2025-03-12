import MeCab
t = MeCab.Tagger()


def analyze_neko():
    """
    neko.txtを形態素解析してリストを返す関数
    
    Returns:
        list: 各形態素を辞書形式で格納したリスト
    """
    # neko.txtを読み込む
    with open('neko.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    
    # MeCabで解析
    mecab_result = t.parse(text)
    
    # 解析結果を形態素ごとに分割
    lines = mecab_result.split('\n')
    
    # 結果を格納するリスト
    result = []
    
    # 各行を解析
    for line in lines:
        # EOSや空行はスキップ
        if line == 'EOS' or line == '':
            continue
        
        # タブで分割して表層形と素性情報を取得
        surface, features = line.split('\t')
        
        # 素性情報をカンマで分割
        features = features.split(',')
        
        # 形態素情報を辞書形式で格納
        morpheme = {
            'surface': surface,      # 表層形
            'base': features[6],     # 基本形
            'pos': features[0],      # 品詞
            'pos1': features[1]      # 品詞細分類1
        }
        
        # 結果リストに追加
        result.append(morpheme)
    
    return result


if __name__ == '__main__':
    # 形態素解析の実行
    neko_morphemes = analyze_neko()
    
    for i, morpheme in enumerate(neko_morphemes[:100]):
        print(f"{i+1}: {{'surface': '{morpheme['surface']}', 'base': '{morpheme['base']}', 'pos': '{morpheme['pos']}', 'pos1': '{morpheme['pos1']}'}}")
