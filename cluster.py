# Param
import sys
image_sets = int(sys.argv[1])
num_clusters = int(sys.argv[2])
iterations = int(sys.argv[3])
limit_to_smallest_cluster = True

# Load data
print("Starting data loading...")
import hickle
data = hickle.load("output.hkl")
print("Loaded data.")

# Create vector array
print("Creating vectors...")
vectors = []
for i in data:	
	vectors.append(i[1].tolist())
	print(i)
print("Created vectors.")

# Create data frame
print("Creating data frame...")
import pandas as pd 
columns = list(range(0, len(vectors[0])))
df = pd.DataFrame(vectors, columns=columns)
print("Created data frame.")

# K means
print("Starting k means...")
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=num_clusters, max_iter=iterations)
kmeans.fit(df)
labels = kmeans.predict(df).tolist()
centroids = kmeans.cluster_centers_
print("K means initialized.")

# Create vector clusters
print("Creating clusters...")
clusters = []
for i in range(0, num_clusters):
	clusters.append([])
removed = 0
for label in labels:
	index = labels.index(label)
	clusters[label].append(vectors[index+removed])	
	labels.remove(label)
	removed += 1
	print(label)
print("Clusters created.")

# Compute distances
print("Computing distances...")
from scipy import spatial
j_sums = [] # We want to maximize the j sum values
for i in range(0, num_clusters):
	j_sum = 0
	cluster = clusters[i]
	center = centroids[i]
	for vector in cluster:
		j_sum += (1 - spatial.distance.cosine(center, vector))
	j_sums.append(j_sum)
	print(j_sum)
print("Distances computed.")

# Extract image set vectors
print("Extracting vectors...")
image_set_vectors = []
for i in range(0, image_sets):
	max_value = max(j_sums)
	best_index = j_sums.index(max_value)
	j_sums.remove(max_value)
	image_set_vectors.append(clusters[best_index])
	print(max_value)
print("Image set vectors extracted.")

# Extract image set names
print("Extracting paths...")
image_set_paths = []
for i in image_set_vectors:
	image_set = []
	for vector in i:	
		index = vectors.index(vector)	
		image_set.append(data[index][0])
		print(index)
	image_set_paths.append(image_set)	
print("Image set paths extracted.")

# Copy images
print("Copying images...")
import os, shutil
root = os.path.join(os.getcwd(), 'output/')
shutil.rmtree(root, ignore_errors=True)
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
ensure_dir(root)
i = 1
smallest_len = []
for paths in image_set_paths:
	smallest_len.append(len(paths))
for paths in image_set_paths:
	sub_path = os.path.join(root, str(i)+'/')
	ensure_dir(sub_path)
	for path in paths:
		if (paths.index(path)+1 > min(smallest_len) and limit_to_smallest_cluster):
			continue
		shutil.copy(path, sub_path+"/"+str(paths.index(path)+1)+".jpg")
		print(path)
	i += 1
print("Copied images (with limiting to smallest cluster).")

print("Script done :)")