import importlib
import matplotlib.pyplot as plt

m30 = importlib.import_module("30")
m35 = importlib.import_module("35")

if __name__ == '__main__':
    # Get the 10 most frequent bases
    frequencies = m35.frequencies()
    words, frequencies = zip(*frequencies)

    # Set the font to a Japanese font
    # https://qiita.com/yniji/items/2f0fbe0a52e3e067c23c
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']


    # Create a log-log plot
    plt.figure(figsize=(10, 6))
    plt.loglog(range(1, len(frequencies) + 1), frequencies, marker='o', linestyle='None')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.title('Log-Log Plot of Word Frequencies')
    plt.grid(True)
    plt.savefig('39.png')
    plt.show()
