import importlib
m30 = importlib.import_module("30")

if __name__ == '__main__':
    neko_morphemes = m30.analyze_neko()
    count = 0
    for i in range(len(neko_morphemes)-2):
        cond0 = neko_morphemes[i]['pos'] == '名詞'
        cond1 = neko_morphemes[i+1]['surface'] == 'の' and neko_morphemes[i+1]['pos'] == '助詞'
        cond2 = neko_morphemes[i+2]['pos'] == '名詞'
        if cond0 and cond1 and cond2:
            count += 1
            print(f"{neko_morphemes[i]['surface']}の{neko_morphemes[i+2]['surface']}")
    print('AのBの個数:', count)
