import time
import numpy as np
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
from collections import defaultdict

def get_country_names():
    """Get a list of country names"""
    # Common country names that are likely to be in the vocabulary
    countries = [
        'Japan', 'China', 'Korea', 'India', 'Thailand', 'Vietnam', 'Indonesia',
        'Germany', 'France', 'Italy', 'Spain', 'England', 'Poland', 'Russia',
        'America', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Chile',
        'Australia', 'Egypt', 'Nigeria', 'Kenya', 'Morocco', 'Turkey',
        'Iran', 'Iraq', 'Israel', 'Jordan', 'Lebanon', 'Syria',
        'Norway', 'Sweden', 'Denmark', 'Finland', 'Netherlands', 'Belgium',
        'Austria', 'Switzerland', 'Greece', 'Portugal', 'Hungary', 'Romania',
        'Bulgaria', 'Croatia', 'Serbia', 'Czech', 'Slovakia', 'Slovenia',
        'Ukraine', 'Belarus', 'Lithuania', 'Latvia', 'Estonia',
        'Afghanistan', 'Pakistan', 'Bangladesh', 'Myanmar', 'Malaysia',
        'Singapore', 'Philippines', 'Cambodia', 'Laos', 'Mongolia',
        'Kazakhstan', 'Uzbekistan', 'Kyrgyzstan', 'Tajikistan', 'Turkmenistan',
        'Algeria', 'Tunisia', 'Libya', 'Sudan', 'Ethiopia', 'Somalia',
        'Ghana', 'Mali', 'Senegal', 'Niger', 'Chad', 'Cameroon',
        'Angola', 'Zambia', 'Zimbabwe', 'Botswana', 'Namibia',
        'Venezuela', 'Colombia', 'Peru', 'Ecuador', 'Bolivia', 'Uruguay',
        'Paraguay', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama',
        'Cuba', 'Jamaica', 'Haiti', 'Dominican', 'Trinidad'
    ]
    return countries

def extract_country_vectors(kv, countries):
    """Extract country vectors from Word2Vec model"""
    country_vectors = []
    valid_countries = []

    for country in countries:
        if country in kv:
            country_vectors.append(kv[country])
            valid_countries.append(country)
        else:
            print(f"Country not found in vocabulary: {country}")

    return np.array(country_vectors), valid_countries

def perform_kmeans_clustering(vectors, k=5):
    """Perform k-means clustering"""
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(vectors)
    return kmeans, clusters

def analyze_clusters(countries, clusters, k=5):
    """Analyze and display clustering results"""
    cluster_groups = defaultdict(list)

    for country, cluster in zip(countries, clusters):
        cluster_groups[cluster].append(country)

    print(f"\nClustering Results (k={k}):")
    print("=" * 50)

    for i in range(k):
        countries_in_cluster = cluster_groups[i]
        print(f"\nCluster {i} ({len(countries_in_cluster)} countries):")
        print(f"  {', '.join(countries_in_cluster)}")

    return cluster_groups

if __name__ == "__main__":
    start = time.time()

    # Load Word2Vec model
    print(f"({time.time() - start:.2f}s) Loading Word2Vec model...")
    kv = KeyedVectors.load_word2vec_format(
        "GoogleNews-vectors-negative300.bin", binary=True)

    # Get country names
    countries = get_country_names()
    print(f"({time.time() - start:.2f}s) Checking {len(countries)} country names...")

    # Extract country vectors
    country_vectors, valid_countries = extract_country_vectors(kv, countries)
    print(f"({time.time() - start:.2f}s) Found {len(valid_countries)} countries in vocabulary")

    if len(valid_countries) == 0:
        print("No countries found in vocabulary!")
        exit(1)

    # Perform k-means clustering
    print(f"({time.time() - start:.2f}s) Performing k-means clustering (k=5)...")
    kmeans, clusters = perform_kmeans_clustering(country_vectors, k=5)

    # Analyze results
    cluster_groups = analyze_clusters(valid_countries, clusters, k=5)

    print(f"\n({time.time() - start:.2f}s) Clustering completed!")
    print(f"Total processing time: {time.time() - start:.2f} seconds")
