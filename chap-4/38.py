import importlib
import matplotlib.pyplot as plt

m30 = importlib.import_module("30")
m35 = importlib.import_module("35")

if __name__ == '__main__':
    # Get the 10 most frequent bases
    frequencies = m35.frequencies()
    frequencies = [freq for _, freq in frequencies]
    frequencies.sort()
    print(frequencies[:10])

    # Set the font to a Japanese font
    # https://qiita.com/yniji/items/2f0fbe0a52e3e067c23c
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']

    plt.figure(figsize=(10, 6))
    plt.hist(frequencies, bins=100)
    plt.xlabel('Frequency')
    plt.ylabel('Frequency of frequency')
    plt.yscale('log')
    plt.title('Plot of Word Frequencies')
    plt.grid(True)
    plt.savefig('38.png')
    plt.show()
