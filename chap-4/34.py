import importlib
m30 = importlib.import_module("30")

if __name__ == '__main__':
    neko_morphemes = m30.analyze_neko()
    longest = 0
    longest_pos = None
    cur = 0
    for i in range(len(neko_morphemes)):
        cond0 = neko_morphemes[i]['pos'] == '名詞'
        if cond0:
            cur += 1
            if cur > longest:
                longest = cur
                longest_pos = i - cur + 1
        else:
            cur = 0
    print('最長の名詞の連接:', longest)
    print([morpheme['surface'] for morpheme in neko_morphemes[longest_pos:longest_pos+longest]])
