import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Constant
CARS_DATASET = "./cars.csv"
LOOPS = 20
MAX_ITERATIONS = 10
INITIALIZE_CLUSTERS = 'k-means++'
CONVERGENCE_TOLERANCE = 0.001
NUM_THREADS = 8


def dataset_to_list_points(dir_dataset):
    """
    Read THE .csv dataset with a set of points and return a list of objects Point
    :param dir_dataset:
    """
    points = list()
    with open(dir_dataset, 'rt') as reader:
        for point in reader:
            a = int(np.asarray(point.split(",")[0]))
            b = float(np.asarray(point.split(",")[10]))
            c = [a,b]
            points.append(c)
    return points


def plot_results(inertials):
    x, y = zip(*[inertia for inertia in inertials])
    plt.plot(x, y, 'ro-', markersize=8, lw=2)
    plt.grid(True)
    plt.xlabel('Num Clusters')
    plt.ylabel('Inertia')
    plt.show()


def select_clusters(dataset, loops, max_iterations, init_cluster, tolerance, num_threads):
    # Read data set
    points = dataset_to_list_points(dataset)
    for i in range(len(points)):
        print(points[i])

    # Object KMeans
    kmeans = KMeans(n_clusters=3, max_iter=max_iterations, init=init_cluster, tol=tolerance, n_jobs=num_threads)

    # Calculate Kmeans
    kmeans.fit(points)
    

    labels=kmeans.predict(points)
    centroids=kmeans.cluster_centers_
    
    colors=["c.","y.","b.","m.","r."]
    
    for i in range(len(points)):
        print("Coordenada: ",points[i]," Label: ",labels[i])
        plt.plot(points[i][0],points[i][1],colors[labels[i]],markersize=10)
    plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=150,linewidth=5,zorder=10)
    plt.grid(True)
    plt.show()
    

select_clusters(CARS_DATASET, LOOPS, MAX_ITERATIONS, INITIALIZE_CLUSTERS, CONVERGENCE_TOLERANCE, NUM_THREADS)
