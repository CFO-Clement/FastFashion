A partir de ce que je vais te donnée, je veux que tu me cree une fonction qui prend en parametre un nom de class de modelle scikit learn et un tableau contenant les algo a utilisé sur cette objet.
Puis je veux que tu utilise c'est algo pour trouver le meillieur nombre de classe. Ensuite je veux que tu utilise la fonction auto_random_search pour trouver les meilleurs parametre pour ce modelle. pour trouvé les autre hyperparametre.
Si la methode pour l'algorythme est None alors utilise seulement aute_random_search.

clusters = ['KMeans', 'DBSCAN', 'GaussianMixture', 'AgglomerativeClustering', 'SpectralClustering', 'OPTICS', 'MeanShift', 'AffinityPropagation', 'Birch', 'MiniSom', 'hdbscan.HDBSCAN']
methods = {
'KMeans': ['Elbow', 'Silhouette', 'Gap Statistic', 'Explained Variance'],
'DBSCAN': None,
'GaussianMixture': None, #['Bayesian Information Criterion (BIC)'],
'AgglomerativeClustering': ['Elbow', 'Silhouette', 'Gap Statistic'],
'SpectralClustering': ['Variance Ratio', 'Gap Statistic'],
'OPTICS': None,
'MeanShift': None,
'AffinityPropagation': None,
'Birch': ['Elbow', 'Explained Variance'],
'MiniSom': None,
'hdbscan.HDBSCAN': None #['HDBSCAN Hierarchy']
}
# Auto Random Search
def auto_random_search(clustering_obj, data, max_clusters, n_iter=10, show=False, **params):
    """
    The function auto_random_search performs a random search for the best hyperparameters of a clustering algorithm using silhouette score as the evaluation metric.

    Parameters:

    clustering_obj: An instance of a clustering algorithm that implements the scikit-learn API.
    data: Input data to be clustered.
    max_clusters: Maximum number of clusters to consider in the search.
    n_iter: Number of parameter combinations to try in the random search.
    show: Boolean flag indicating whether to display a plot of the silhouette scores for each parameter combination. Default is False.
    **params: Variable number of keyword arguments specifying the hyperparameters to be tuned in the search.
    Returns:

    best_params: Dictionary containing the best set of hyperparameters found in the search.
    """
    return best_params

#Auto Variance Ratio Method
def auto_var_ratio(clustering_obj, data, max_clusters, show=False):
    """The function auto_var_ratio performs clustering using the Variance Ratio Method and returns the optimal number of clusters based on the Calinski-Harabasz score.

    Parameters:

    clustering_obj: An instance of a clustering algorithm that implements the scikit-learn API.
    data: Input data to be clustered.
    max_clusters: Maximum number of clusters to consider in the search.
    show: Boolean flag indicating whether to display a plot of the Calinski-Harabasz scores for each number of clusters. Default is False.
    Returns:

    optimal_cluster_size: The optimal number of clusters found by the Variance Ratio Method based on the Calinski-Harabasz score.
    """
    return optimal_cluster_size

#Auto ExplainedVar
def auto_explained_var(clustering_obj, data, max_clusters, show=False):
    """
    The function auto_explained_var performs clustering using the Explained Variance Method and returns the optimal number of clusters based on the Calinski-Harabasz score.

    Parameters:

    clustering_obj: An instance of a clustering algorithm that implements the scikit-learn API.
    data: Input data to be clustered.
    max_clusters: Maximum number of clusters to consider in the search.
    show: Boolean flag indicating whether to display a plot of the Calinski-Harabasz scores for each number of clusters. Default is False.
    Returns:

    optimal_cluster_size: The optimal number of clusters found by the Explained Variance Method based on the Calinski-Harabasz score.
    """
    return optimal_cluster_size

#Auto Silhouette Method
def auto_silhouette(clustering_obj, data, max_clusters, show=False):
    """
    The function auto_silhouette performs clustering using the Silhouette Method and returns the optimal number of clusters based on the Silhouette score.

    Parameters:

    clustering_obj: An instance of a clustering algorithm that implements the scikit-learn API.
    data: Input data to be clustered.
    max_clusters: Maximum number of clusters to consider in the search.
    show: Boolean flag indicating whether to display a plot of the Silhouette scores for each number of clusters. Default is False.
    Returns:

    optimal_cluster_size: The optimal number of clusters found by the Silhouette Method based on the Silhouette score.
    """
    return optimal_cluster_size

#Auto Elbow Method
def auto_elbow(clustering_obj, data, max_clusters, show=False):
    """
    The function auto_elbow performs clustering using the Elbow Method and returns the optimal number of clusters based on the within-cluster sum of squares.

    Parameters:

    clustering_obj: An instance of a clustering algorithm that implements the scikit-learn API.
    data: Input data to be clustered.
    max_clusters: Maximum number of clusters to consider in the search.
    show: Boolean flag indicating whether to display a plot of the within-cluster sum of squares for each number of clusters. Default is False.
    Returns:

    elbow_point: The optimal number of clusters found by the Elbow Method based on the within-cluster sum of squares.

    """
    return elbow_point
