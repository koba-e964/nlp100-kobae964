import time
import numpy as np
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
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
        'Cuba', 'Jamaica', 'Haiti', 'Dominican', 'Trinidad',
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

def perform_tsne(vectors: np.ndarray, perplexity: float = 30.0, n_iter: int = 1000, random_state: int = 42) -> np.ndarray:
    """Perform t-SNE dimensionality reduction"""
    tsne = TSNE(
        n_components=2,
        perplexity=perplexity,
        max_iter=n_iter,
        random_state=random_state,
        verbose=1,
    )

    tsne_results = tsne.fit_transform(vectors)
    return tsne_results

def visualize_tsne(tsne_results: np.ndarray, country_names: list[str], save_path: str = None):
    """Visualize t-SNE results"""
    plt.figure(figsize=(16, 12))

    # Create scatter plot
    plt.scatter(tsne_results[:, 0], tsne_results[:, 1], alpha=0.7, s=100)

    # Add country labels
    for i, country in enumerate(country_names):
        plt.annotate(
            country,
            (tsne_results[i, 0], tsne_results[i, 1]),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=9,
            alpha=0.8,
        )

    plt.title('t-SNE Visualization of Country Word Vectors', fontsize=16)
    plt.xlabel('t-SNE Dimension 1', fontsize=14)
    plt.ylabel('t-SNE Dimension 2', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"t-SNE visualization saved as: {save_path}")

def analyze_clusters_from_tsne(tsne_results: np.ndarray, country_names: list[str], n_clusters: int = 5):
    """Analyze clusters using k-means on t-SNE results"""
    from sklearn.cluster import KMeans
    from collections import defaultdict

    # Perform k-means on t-SNE results
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(tsne_results)

    # Group countries by cluster
    cluster_groups = defaultdict(list)
    for country, cluster in zip(country_names, clusters):
        cluster_groups[cluster].append(country)

    print(f"\nClusters identified from t-SNE visualization (k={n_clusters}):")
    print("=" * 60)

    for cluster_id, countries in cluster_groups.items():
        print(f"\nCluster {cluster_id} ({len(countries)} countries):")
        print(f"  {', '.join(countries)}")

    return cluster_groups

def visualize_tsne_with_clusters(tsne_results: np.ndarray, country_names: list[str], n_clusters: int = 5, save_path: str = None):
    """Visualize t-SNE results with cluster colors"""
    from sklearn.cluster import KMeans

    # Perform k-means on t-SNE results
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(tsne_results)

    plt.figure(figsize=(16, 12))

    # Create scatter plot with cluster colors
    colors = plt.cm.Set1(np.linspace(0, 1, n_clusters))
    for i in range(n_clusters):
        mask = clusters == i
        plt.scatter(
            tsne_results[mask, 0], 
            tsne_results[mask, 1], 
            c=[colors[i]], 
            label=f'Cluster {i}',
            alpha=0.7, 
            s=100,
        )

    # Add country labels
    for i, country in enumerate(country_names):
        plt.annotate(
            country,
            (tsne_results[i, 0], tsne_results[i, 1]),
            xytext=(5, 5),
            textcoords='offset points',
            fontsize=9,
            alpha=0.8
        )

    plt.title(f't-SNE Visualization with {n_clusters} Clusters', fontsize=16)
    plt.xlabel('t-SNE Dimension 1', fontsize=14)
    plt.ylabel('t-SNE Dimension 2', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"t-SNE clustered visualization saved as: {save_path}")

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

    # Perform t-SNE
    print(f"({time.time() - start:.2f}s) Performing t-SNE dimensionality reduction...")
    tsne_results = perform_tsne(country_vectors, perplexity=min(30.0, len(valid_countries) - 1))

    # Visualize t-SNE results
    print(f"({time.time() - start:.2f}s) Creating t-SNE visualization...")
    visualize_tsne(tsne_results, valid_countries, "country_tsne.png")

    # Visualize with clusters
    print(f"({time.time() - start:.2f}s) Creating clustered t-SNE visualization...")
    visualize_tsne_with_clusters(tsne_results, valid_countries, n_clusters=5, save_path="country_tsne_clustered.png")

    # Analyze clusters
    analyze_clusters_from_tsne(tsne_results, valid_countries, n_clusters=5)

    print(f"\n({time.time() - start:.2f}s) t-SNE visualization completed!")
    print(f"Total processing time: {time.time() - start:.2f} seconds")
