import importlib
import matplotlib.pyplot as plt

m30 = importlib.import_module("30")

if __name__ == '__main__':
    neko_morphemes = m30.analyze_neko()
    freq = {}
    for i in range(len(neko_morphemes)-1):
        if neko_morphemes[i]['surface'] == '猫':
            base = neko_morphemes[i+1]['base']
            if base in freq:
                freq[base] += 1
            else:
                freq[base] = 1
    bases_freq = list(freq.items())
    bases_freq.sort(key=lambda x: x[1], reverse=True)
    print('猫と共起する単語最頻 10 個:')
    for i, (base, freq) in enumerate(bases_freq[:10]):
        print(f"{i+1}: {base} ({freq}回)")

    # Set the font to a Japanese font
    # https://qiita.com/yniji/items/2f0fbe0a52e3e067c23c
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']


    # Plot the histogram
    words, frequencies = zip(*bases_freq[:10])
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title('Top 10 Most Frequent Words Co-occurring with "猫"')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('37.png')
    plt.show()
