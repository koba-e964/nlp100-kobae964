import time
import numpy as np
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

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

def extract_country_vectors(kv: KeyedVectors, countries: list[str]) -> tuple[np.ndarray, list[str]]:
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

def perform_ward_clustering(vectors: np.ndarray) -> np.ndarray:
    """Perform Ward method hierarchical clustering"""
    linkage_matrix = linkage(vectors, method='ward')
    return linkage_matrix

def create_dendrogram(linkage_matrix: np.ndarray, country_names: list[str], save_path: str = None):
    """Create and display dendrogram"""
    plt.figure(figsize=(20, 10))

    # Create dendrogram
    dendrogram(
        linkage_matrix,
        labels=country_names,
        orientation='top',
        leaf_rotation=90,
        leaf_font_size=10
    )

    plt.title('Hierarchical Clustering of Countries (Ward Method)', fontsize=16)
    plt.xlabel('Countries', fontsize=14)
    plt.ylabel('Distance', fontsize=14)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Dendrogram saved as: {save_path}")

def analyze_clustering_at_level(linkage_matrix: np.ndarray, country_names: list[str], n_clusters: int = 5):
    """Analyze clustering results at a specific number of clusters"""
    from scipy.cluster.hierarchy import fcluster

    clusters = fcluster(linkage_matrix, n_clusters, criterion='maxclust')

    cluster_groups = {}
    for i in range(1, n_clusters + 1):
        cluster_groups[i] = []

    for country, cluster in zip(country_names, clusters):
        cluster_groups[cluster].append(country)

    print(f"\nClustering Results at {n_clusters} clusters:")
    print("=" * 60)

    for cluster_id, countries in cluster_groups.items():
        print(f"\nCluster {cluster_id} ({len(countries)} countries):")
        print(f"  {', '.join(countries)}")

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

    # Perform Ward method hierarchical clustering
    print(f"({time.time() - start:.2f}s) Performing Ward method clustering...")
    linkage_matrix = perform_ward_clustering(country_vectors)

    # Create and display dendrogram
    print(f"({time.time() - start:.2f}s) Creating dendrogram...")
    create_dendrogram(linkage_matrix, valid_countries, "country_dendrogram.png")

    # Analyze clustering at different levels
    analyze_clustering_at_level(linkage_matrix, valid_countries, n_clusters=5)
    analyze_clustering_at_level(linkage_matrix, valid_countries, n_clusters=3)

    print(f"\n({time.time() - start:.2f}s) Ward clustering completed!")
    print(f"Total processing time: {time.time() - start:.2f} seconds")
