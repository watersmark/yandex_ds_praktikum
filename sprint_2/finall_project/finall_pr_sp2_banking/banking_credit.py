import numpy as np
import scipy.spatial.distance


vectors = np.array([[7, 1, 5, 3], [5, 5, 4, 2], [3, 4, 5, 4]])


dist = scipy.spatial.distance.pdist(vectors, 'cosine')
print(dist)
