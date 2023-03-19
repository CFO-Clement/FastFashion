clusters = ['KMeans', 'DBSCAN', 'GaussianMixture', 'AgglomerativeClustering', 'SpectralClustering', 'OPTICS', 'MeanShift', 'AffinityPropagation', 'Birch', 'MiniSom', 'hdbscan.HDBSCAN']
methods = {
    'KMeans': {
        'tuning' : ['Elbow', 'Silhouette', 'Gap Statistic', 'Explained Variance'],
        'args': {"n_clusters": list(range(2, 11)), 
                 "init": ['k-means++', 'random'], 
                 "max_iter": list(range(50, 501, 50)), 
                 "tol": [1e-3, 1e-4, 1e-5], 
                 "algorithm": ['auto', 'full', 'elkan']}
    },
    'DBSCAN': {
        'tuning' : None,
        'args': {"eps": np.linspace(0.1, 1.0, num=10), 
                 "min_samples": range(2, 10), 
                 "metric": ['euclidean', 'manhattan', 'chebyshev', 'cosine']}
    },
    'GaussianMixture': {
        'tuning' : None, #['Bayesian Information Criterion (BIC)'],
        'args': {"n_components": list(range(2, 11)), 
                 "covariance_type": ['full', 'tied', 'diag', 'spherical'], 
                 "max_iter": list(range(50, 501, 50)), 
                 "tol": [1e-3, 1e-4, 1e-5]}
    },
    'AgglomerativeClustering': { 
        'tuning' : ['Elbow', 'Silhouette', 'Gap Statistic'],
        'args': {"n_clusters": list(range(2, 11)), 
                 "linkage": ['ward', 'complete', 'average'], 
                 "affinity": ['euclidean', 'manhattan', 'cosine']}
    },
    'SpectralClustering': {
        'tuning' : ['Variance Ratio', 'Gap Statistic'],
        'args': {"n_clusters": list(range(2, 11)), 
                 "affinity": ['nearest_neighbors', 'rbf'], 
                 "gamma": [1e-2, 1e-3, 1e-4], 
                 "n_neighbors": list(range(5, 21))}
    },
    'OPTICS': {
        'tuning' : None,
        'args': {"min_samples": list(range(2, 11)), 
                 "metric": ['euclidean', 'manhattan', 'chebyshev', 'cosine']}
    },
    'MeanShift': {
        'tuning' : None,
        'args': {"bandwidth": list(range(1, 11)), 
                 "bin_seeding": [True, False]}
    },
    'AffinityPropagation': {
        'tuning' : None,
        'args': {"damping": [0.5, 0.6, 0.7, 0.8, 0.9], 
                 "convergence_iter": list(range(10, 101, 10))}
    },
    'Birch': {
        'tuning' : ['Elbow', 'Explained Variance'],
        'args': {"n_clusters": list(range(2, 11)), 
                 "threshold": [0.1, 0.2, 0.3, 0.4], 
                 "branching_factor": list(range(10, 101, 10))}
    },
        'MiniSom': {
        'tuning' : None,
        'args': {"x": [10, 20, 30, 40, 50], 
                 "y": [10, 20, 30, 40, 50], 
                 "sigma": [0.1, 0.2, 0.3, 0.4], 
                 "learning_rate": [0.1, 0.2, 0.3, 0.4], 
                 "neighborhood_function": ['gaussian', 'bubble', 'triangle']}
    },
    'hdbscan.HDBSCAN': {
        'tuning' : ['HDBSCAN Hierarchy'],
        'args': {"min_cluster_size": [2, 5, 10, 20], 
                 "min_samples": list(range(1, 11)), 
                 "metric": ['euclidean', 'manhattan', 'chebyshev', 'cosine'], 
                 "alpha": [1.0, 1.5, 2.0]}
    }
}
df = clothes_df.drop(['Type', 'Environmental Impact Score', 'Animal Welfare Score', 'Human Welfare Score', 'Social Responsibility Score'], axis=1)
scaler = StandardScaler()
df_normalized = scaler.fit_transform(df)

def auto_elbow(clustering_obj, data, number_clusters, show=False):
    max_clusters = max(number_clusters)
    sse = []
    for n_clusters in number_clusters:
        clustering_obj.set_params(n_clusters=n_clusters)
        clustering_obj.fit(data)
        sse.append(clustering_obj.inertia_)

    sse = np.array(sse)
    diff = np.diff(sse)
    diff_r = diff[1:] / diff[:-1]
    elbow_point = np.argmin(diff_r) + 2
    return elbow_point

def auto_silhouette(clustering_obj, data, number_clusters, show=False):
    max_clusters = max(number_clusters)
    silhouette_scores = []
    for n_clusters in number_clusters:
        clustering_obj.set_params(n_clusters=n_clusters, n_init=10)
        clustering_obj.fit(data)
        silhouette_scores.append(silhouette_score(data, clustering_obj.labels_))
    
    silhouette_scores = np.array(silhouette_scores)
    optimal_cluster_idx = np.argmax(silhouette_scores)
    optimal_cluster_size = optimal_cluster_idx + 2
    return optimal_cluster_size

def auto_explained_var(clustering_obj, data, number_clusters, show=False):
    max_clusters = max(number_clusters)
    ch_scores = []
    for n_clusters in number_clusters:
        clustering_obj.set_params(n_clusters=n_clusters, n_init=10)
        clustering_obj.fit(data)
        ch_scores.append(calinski_harabasz_score(data, clustering_obj.labels_))

    ch_scores = np.array(ch_scores)
    optimal_cluster_idx = np.argmax(ch_scores)
    optimal_cluster_size = optimal_cluster_idx + 2
    return optimal_cluster_size

def auto_BIC(gmm_obj, data, number_clusters, show=False):
    print("l'ordi kiif pas de fous")
    return 3
    max_clusters = max(number_clusters)
    bic_scores = []
    for n_clusters in number_clusters:
        gmm_obj = GaussianMixture(n_components=n_clusters, n_init=10)
        gmm_obj.fit(data)
        bic_scores.append(gmm_obj.bic(data))

    bic_scores = np.array(bic_scores)
    optimal_cluster_idx = np.argmin(bic_scores)
    optimal_cluster_size = optimal_cluster_idx + 1
    return optimal_cluster_size

def auto_var_ratio(clustering_obj, data, number_clusters, show=False):
    max_clusters = max(number_clusters)
    vr_scores = []
    for n_clusters in number_clusters:
        clustering_obj.set_params(n_clusters=n_clusters, n_init=10)
        clustering_obj.fit(data)
        vr_scores.append(calinski_harabasz_score(data, clustering_obj.labels_))

    vr_scores = np.array(vr_scores)
    optimal_cluster_idx = np.argmax(vr_scores)
    optimal_cluster_size = optimal_cluster_idx + 2
    return optimal_cluster_size

def auto_random_search(clustering_obj, data, n_iter=10, show=False, override_cluster=None, **params):
    best_score = -np.inf
    best_params = None
    best_obj = None
    
    n_clusters_key = "n_clusters"
    if n_clusters_key not in params:
        raise ValueError(f"'{n_clusters_key}' parameter must be specified in 'args' for {clustering_obj.__class__.__name__}")
    
    max_clusters = params[n_clusters_key][-1]
    
    if override_cluster is not None:
        force_cluster = True
        param_dist = {k: list(set(v)) if k == n_clusters_key else v for k, v in params.items()}
        param_dist[n_clusters_key] = [override_cluster]
    else:
        force_cluster = False
        param_dist = {k: list(set(v)) if k == n_clusters_key else v for k, v in params.items()}
        param_dist[n_clusters_key] = list(set(range(2, max_clusters + 1)))
    
    param_sampler = ParameterSampler(param_dist, n_iter=n_iter)
    
    scores = []
    parameters = []
    
    for params in param_sampler:
        tmp_clustering_obj = clone(clustering_obj)
        tmp_clustering_obj.set_params(**params)
        tmp_clustering_obj.fit(data)
        
        score = silhouette_score(data, tmp_clustering_obj.labels_)
        scores.append(score)
        parameters.append(params)
        
        if score > best_score:
            best_score = score
            best_params = params
            best_obj = tmp_clustering_obj
    return best_params

def fine_tune_algo(cluster_name, methods, data, n_iter=10, show=True):
    try:
        print(f"Fine tuning {cluster_name} algorithm...")
        cluster_obj = None
        if cluster_name == 'KMeans':
            cluster_obj = KMeans()
        elif cluster_name == 'DBSCAN':
            cluster_obj = DBSCAN()
        elif cluster_name == 'GaussianMixture':
            cluster_obj = GaussianMixture()
        elif cluster_name == 'AgglomerativeClustering':
            cluster_obj = AgglomerativeClustering()
        elif cluster_name == 'SpectralClustering':
            cluster_obj = SpectralClustering()
        elif cluster_name == 'OPTICS':
            cluster_obj = OPTICS()
        elif cluster_name == 'MeanShift':
            cluster_obj = MeanShift()
        elif cluster_name == 'AffinityPropagation':
            cluster_obj = AffinityPropagation()
        elif cluster_name == 'Birch':
            cluster_obj = Birch()
        elif cluster_name == 'MiniSom':
            cluster_obj = MiniSom()
        elif cluster_name == 'HDBSCAN':
            cluster_obj = hdbscan.HDBSCAN()
        else:
            raise Exception("Unknown clustering algorithm")
        
        method_funcs = {
            'Elbow': auto_elbow,
            'Silhouette': auto_silhouette,
            'Gap Statistic': None,
            'Explained Variance': auto_explained_var,
            'Bayesian Information Criterion (BIC)': None,
            'Variance Ratio': auto_var_ratio,
            'OPTICS Hierarchy': None,
            'HDBSCAN Hierarchy': None
            }
        
        if methods[cluster_name]['tuning'] is None:
            print(f"Performing automatic tuning with random search for {n_iter} iterations...")
            best_params = auto_random_search(cluster_obj, df, n_iter=n_iter, show=show, **methods[cluster_name]['args'])
        else:
            print("Performing tuning with the following methods:")
            print(methods[cluster_name]['tuning'])
            cluster_numbers = []
            for method in methods[cluster_name]['tuning']:
                if method_funcs[method] is None:
                    print(f"Performing automatic tuning with random search for {n_iter} iterations using {method} method...")
                    cluster_numbers.append(auto_random_search(cluster_obj, df, n_iter=n_iter, show=show, **methods[cluster_name]['args'])['n_clusters'])
                else:
                    print(f"Performing tuning with {method} method...")
                    cluster_numbers.append(method_funcs[method](cluster_obj, df, number_clusters=methods[cluster_name]['args']['n_clusters'], show=show))
            best_cluster_numbers = int(sum(cluster_numbers) / len(cluster_numbers))
            print(f"Performing automatic tuning with random search for {n_iter} iterations using the best cluster number ({best_cluster_numbers}) from previous tuning methods...")
            best_params = auto_random_search(cluster_obj, df, n_iter=n_iter, show=show, override_cluster=best_cluster_numbers, **methods[cluster_name]['args'])
        return best_params
    except Exception as e:
        print(f"--KO-- Error while fine tuning {cluster_name} algorithm")
        pp(e)
        return 'Failed'

best_params = {}
for algo in clusters:
    best_params[algo] = fine_tune_algo(cluster_name=algo, methods=methods, data=df, n_iter=10, show=True)
