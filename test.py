# Auto Random Search Method
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

    if show:
        sns.set(style="whitegrid")

        fig, ax = plt.subplots(figsize=(10, 6))
        x = range(1, n_iter + 1)
        ax.bar(x, scores, tick_label=[str(p[n_clusters_key]) for p in parameters])
        ax.set_xlabel('Parameters', fontsize=14)
        ax.set_ylabel('Silhouette Score', fontsize=14)
        ax.set_title(f"Random Search - {clustering_obj.__class__.__name__}", fontsize=16)

        optimal_idx = np.argmax(scores)
        ax.bar(optimal_idx + 1, scores[optimal_idx], color='red', label="Best Score")
        ax.legend(fontsize=12)
        if force_cluster:
            fig.savefig(f"images/{clustering_obj.__class__.__name__}/{clustering_obj.__class__.__name__}_Random_Search_Forced.svg")
        else:
            fig.savefig(f"images/{clustering_obj.__class__.__name__}/{clustering_obj.__class__.__name__}_Random_Search.svg")
        fig.show()


    return best_params

ValueError                                Traceback (most recent call last)
Cell In[96], line 2
      1 # Test fine tuning
----> 2 best = fine_tune_algo(cluster_name='AgglomerativeClustering', methods=methods, data=df, n_iter=10, show=True)
      3 print(best)

Cell In[94], line 51, in fine_tune_algo(cluster_name, methods, data, n_iter, show)
     49 if method_funcs[method] is None:
     50     print(f"Performing automatic tuning with random search for {n_iter} iterations using {method} method...")
---> 51     cluster_numbers.append(auto_random_search(cluster_obj, df, n_iter=n_iter, show=show, **methods[cluster_name]['args'])['n_clusters'])
     52 else:
     53     print(f"Performing tuning with {method} method...")

Cell In[93], line 46, in auto_random_search(clustering_obj, data, n_iter, show, override_cluster, **params)
     44 fig, ax = plt.subplots(figsize=(10, 6))
     45 x = range(1, n_iter + 1)
---> 46 ax.bar(x, scores, tick_label=[str(p[n_clusters_key]) for p in parameters])
     47 ax.set_xlabel('Parameters', fontsize=14)
     48 ax.set_ylabel('Silhouette Score', fontsize=14)

File /opt/homebrew/anaconda3/envs/projet-ia-env/lib/python3.11/site-packages/matplotlib/__init__.py:1442, in _preprocess_data..inner(ax, data, *args, **kwargs)
   1439 @functools.wraps(func)
   1440 def inner(ax, *args, data=None, **kwargs):
   1441     if data is None:
...
    425     # ironically, np.broadcast does not properly handle np.broadcast
    426     # objects (it treats them as scalars)
    427     # use broadcasting to avoid allocating the full array

ValueError: shape mismatch: objects cannot be broadcast to a single shape.  Mismatch is between arg 0 with shape (10,) and arg 1 with shape (9,).
