import importlib
import matplotlib.pyplot as plt

m30 = importlib.import_module("30")
m35 = importlib.import_module("35")

if __name__ == '__main__':
    # Get the 10 most frequent bases
    most_frequent_bases = m35.frequencies()[:10]
    words, frequencies = zip(*most_frequent_bases)

    # Set the font to a Japanese font
    # https://qiita.com/yniji/items/2f0fbe0a52e3e067c23c
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Noto Sans CJK JP']


    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title('Top 10 Most Frequent Verb Bases')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('36.png')
    plt.show()
