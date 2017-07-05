import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import time

#reading the file
df = pd.read_csv('exercise-1.csv',delimiter=',',skipinitialspace=True)

# creating a Node class for our linked list
class Node(object):
    # creates a constructor that takes in two arguments
    def __init__(self, data, next=None):

        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

#linked list class that we implement as data structure for algorithm
class LinkedList(object):

    def __init__(self):

        self.head = None
        self.size = 0


    def append(self, data):
            if not self.head:
                n = Node(data)
                self.head = n
                return
            else:
                n = self.head

                while n.next != None:
                    n = n.next

                new_node = Node(data)
                n.next = new_node;
                return


    def isEmpty(self):
        return not self.head

    def printList(self):
        n = self.head

        while n:
            print str(n)
            n = n.next

ll = LinkedList()
x = []
for elem in x:
    ll.append(elem)
y = []
for elem in y:
    ll.append(elem)

x.extend(np.around(df['x'],decimals=1)) # assigning the first column values to the array
y.extend(np.around(df['y'],decimals=1)) # assigning the second column values to the array
# formatting the array so every element in it is to 2 decimal places
formattedX=['%.2f' % elem for elem in x]
formattedY=['%.2f' % elem for elem in y]

# the matrix is the new array that we pass to the k-means class
newX = df.as_matrix()

#plot original to show without clusters
plt.scatter(formattedX,formattedY)
plt.title('Original Unclustered Data')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

colors = 10*["g","r","c","b","k"]

class K_Means:
    # toleraence is the percentage of how much the centroid is going to move, max_iter is the max iterations the program will run, and k is the number of clusters
    def __init__(self, k = 4, tolerance = 0.001, max_iter = 300):
        self.k = k
        self.tolerance = tolerance
        self.max_iter = max_iter
        start = time.time()

        #keeps a constant number of centroids to move
    def amnt_of_centroids(self, data):
        self.centroids = {} #empty dictionary to store centroids

        # iterating through data, takes the first two data points as centroids to use
        for i in range(self.k):
            self.centroids[i] = data[i]

        # empties the centroids every time the centroid moves, so empty for every iteration
        for i in range(self.max_iter):
            self.clusters = {} #empty dictionary to store new centroids

            # iterating through centroids keys to equal empty list
            for j in range (self.k):
                self.clusters[j] = [] #empty list of data set values

            # populating the empty list created above/ giving it values
            for dataset in data:
                # calculates the distance between the data and the centroid
                distances = [ np.linalg.norm(dataset - self.centroids[i[0]]) for i in enumerate(self.centroids)]
                key = distances.index( min(distances))  # returns the lowest index in the list, so the first element can be used
                self.clusters[key].append(dataset)  # adds the new centroid found to the dictionary

            # comparing the two centroids, to see how much they have changed
            prev_centroids = dict(self.centroids)

            for key in self.clusters:
                # takes the mean of each cluster to calculate new centroid of the cluster
                self.centroids[key] = np.average(self.clusters[key], axis = 0)

            optimized = True

            # if any of the centroids in their movement move more than the tolerance (0.001), we say we are not optimized
            for i in self.centroids:
                original_centroid = prev_centroids[i]
                current_centroid = self.centroids[i]

                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tolerance:
                    optimized = False

                # this will break the for loop and stop us from running every single maximum iteration
                # If this is not the case it will continue through the for loop until it reaches the maximum iteration and at that time whatever the centroid is. This is our final centroid
                if optimized:
                    break

        end = time.time()
        print "time without plot:", end - start


k = K_Means()
start = time.time()
k.amnt_of_centroids(newX)

# plots the centroids
for centroid in k.centroids:
    plt.scatter(k.centroids[centroid][0] , k.centroids[centroid][1], marker = "*", color = "k", s = 150)

# Classifies which color to use for each clusters
for key in k.clusters:
    color = colors[key]
    # plots the clusters
    for dataset in k.clusters[key]:
        plt.scatter(dataset[0], dataset[1], marker = "o", color = color, linewidths = 2)

# plots the clustered cata
plt.title('Clustered data')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.savefig("kmeans.png",format='png',bbox_inches='tight', dpi=300)
end = time.time()
print "total time:", end-start
plt.show()
