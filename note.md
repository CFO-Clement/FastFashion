Code fonctionne correctement jusqu'au fine tunning inclut.
Il manque juste a tester le meilleure modèle avec les best params
Ensuite, tres rapidement, il faudrait faire un inpute dynamique pour la partie "collecte de donnée"
Enfin, il faudrait rediger le rapport.

{'AgglomerativeClustering': {'Score': 0.48896146024604376,
                             'affinity': 'euclidean',
                             'linkage': 'ward',
                             'n_clusters': 2},
 'Birch': {'Score': 0.5242323495067391,
           'branching_factor': 10,
           'n_clusters': 2,
           'threshold': 0.4},
 'KMeans': {'Score': 0.5334797205018613,
            'algorithm': 'auto',
            'init': 'k-means++',
            'max_iter': 100,
            'n_clusters': 2,
            'tol': 0.0001},
 'MiniBatchKMeans': {'Score': 0.5350511543312847,
                     'batch_size': 10,
                     'init': 'k-means++',
                     'max_iter': 200,
                     'n_clusters': 2,
                     'tol': 1e-05},
 'SpectralBiclustering': {'Score': 0.5283535074392304,
                          'method': 'bistochastic',
                          'n_clusters': 2},
 'SpectralClustering': {'Score': 0.5334797205018613,
                        'affinity': 'rbf',
                        'gamma': 0.0001,
                        'n_clusters': 2,
                        'n_neighbors': 8},
 'SpectralCoclustering': {'Score': 0.42685121184530694, 'n_clusters': 2}}