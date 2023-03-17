import numpy as np
from collections import Counter

def calc_dist(a, b):
	"""
	Function to calculate euclidean distance of 2 points
	"""
	return np.linalg.norm(np.array(a) - np.array(b))

def knn(x_train, y_train, x_test, k= 1):
	"""
	Function to make an inference of knn algorithm
	
	Parameters:
	- x_train (list of tuple): features of training data (group of points, each point must have the same size)
	- y_train (list): labels of training data
	- x_test: features of testing data (1 points with size of points is the same as each point in x_train)
	- k: number of nearest points for which we get the predicted class from
	
	Return:
	- pred (any data type): predicted class
	"""

	# Initialize distances list
	distances = list()

	# Calculate distances from x_test to each of x_train
	for i in x_train:
		distances.append(calc_dist(i, x_test))
	
	# Order the distances (ascending, nearest to farthest)
	ordered_distances_index = np.flip(np.argsort(distances))

	# Get the predicted class/ label based on label with max occurances on top k distances
	pred = Counter(y_train[i] for i in ordered_distances_index).most_common()[0][0]

	# Return the predicted class
	return pred

x_train = [(1,2), (4,5), (3,4)]
y_train = ['A', 'A', 'B']
x_test = (5,6)

print(f"{x_test} belong to class: ", knn(x_train, y_train, x_test, 3))