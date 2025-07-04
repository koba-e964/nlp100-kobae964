import time
from gensim.models import KeyedVectors

def read_combined_ssv(filename) -> list[list[str]]:
    """Read words"""
    data = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        # 1行ずつ読み込み、空白で分割してdataに追加
        for line in file:
            line = line.strip()
            if not line or line.startswith(':'):
                continue
            parts = line.split()
            data.append(parts)
    
    return data

if __name__ == "__main__":
    start = time.time()
    kv = KeyedVectors.load_word2vec_format(
        "GoogleNews-vectors-negative300.bin", binary=True)

    word_pairs = read_combined_ssv("questions-words.txt")
    
    # Try finding similar words for first few entries
    print(f"({time.time() - start:.2f}s) Loaded {len(word_pairs)} word pairs:")
    for i, words in enumerate(word_pairs[:10]):
        vec = -kv[words[0]] + kv[words[1]] + kv[words[2]]
        sim = kv.similar_by_vector(vec, 1)
        print(f"({time.time() - start:.2f}s) {i+1}: {words[3]} {sim[0]}")
