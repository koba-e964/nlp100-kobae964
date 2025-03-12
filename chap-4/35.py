import importlib
m30 = importlib.import_module("30")

def frequencies() -> list[tuple[str, int]]:
    neko_morphemes = m30.analyze_neko()
    bases = [morpheme['base'] for morpheme in neko_morphemes if morpheme['pos'] == '動詞']
    bases_freq = {}
    for base in bases:
        if base in bases_freq:
            bases_freq[base] += 1
        else:
            bases_freq[base] = 1
    result = list(bases_freq.items())
    result.sort(key=lambda x: x[1], reverse=True)
    return result

if __name__ == '__main__':
    bases_freq = frequencies()
    print(f'基本形の種類数: {len(bases_freq)}')
    print('基本形の出現頻度（最頻出10個）:')
    for i, (base, freq) in enumerate(bases_freq[:10]):
        print(f"{i+1}: {base} ({freq}回)")
