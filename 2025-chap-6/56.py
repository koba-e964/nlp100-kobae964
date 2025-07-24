import csv
import time
from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr

def read_combined_csv(filename):
    """Read word similarity data from CSV"""
    word_pairs = []
    human_scores = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        
        for row in reader:
            word1, word2, score = row
            word_pairs.append((word1, word2))
            human_scores.append(float(score))
    
    return word_pairs, human_scores

def calculate_word2vec_similarities(kv, word_pairs):
    """Calculate cosine similarities using Word2Vec"""
    similarities = []
    valid_pairs = []
    valid_human_scores = []
    
    for i, (word1, word2) in enumerate(word_pairs):
        try:
            # Calculate cosine similarity
            similarity = kv.similarity(word1, word2)
            similarities.append(similarity)
            valid_pairs.append((word1, word2))
            valid_human_scores.append(human_scores[i])
        except KeyError as e:
            print(f"Word not found in vocabulary: {e}")
            continue
    
    return similarities, valid_pairs, valid_human_scores

if __name__ == "__main__":
    start = time.time()
    
    # Load Word2Vec model
    print(f"({time.time() - start:.2f}s) Loading Word2Vec model...")
    kv = KeyedVectors.load_word2vec_format(
        "GoogleNews-vectors-negative300.bin", binary=True)
    
    # Read word similarity data
    print(f"({time.time() - start:.2f}s) Reading word similarity data...")
    word_pairs, human_scores = read_combined_csv("combined.csv")
    
    # Calculate Word2Vec similarities
    print(f"({time.time() - start:.2f}s) Calculating Word2Vec similarities...")
    w2v_similarities, valid_pairs, valid_human_scores = calculate_word2vec_similarities(kv, word_pairs)
    
    # Calculate Spearman correlation
    if len(w2v_similarities) > 0:
        correlation, p_value = spearmanr(valid_human_scores, w2v_similarities)
        print(f"({time.time() - start:.2f}s) Results:")
        print(f"  Valid pairs: {len(valid_pairs)}/{len(word_pairs)}")
        print(f"  Spearman correlation: {correlation:.4f}")
        print(f"  P-value: {p_value:.4f}")
        
        # Show some examples
        print(f"\nFirst 10 comparisons:")
        for i in range(min(10, len(valid_pairs))):
            word1, word2 = valid_pairs[i]
            human_score = valid_human_scores[i]
            w2v_score = w2v_similarities[i]
            print(f"  {word1}-{word2}: Human={human_score:.2f}, Word2Vec={w2v_score:.4f}")
    else:
        print("No valid word pairs found in vocabulary")