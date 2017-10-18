#Code to extract GPS data from file and perform clustering on it.
import numpy as np
from sklearn.cluster import KMeans, DBSCAN

GPS_data=[]

#Read in the GPS data from the file and store each coordinate as a record in a list
with open('GPS_data/GPS_data.txt','r') as f:
    for line in f:
        record=[float(line.split()[0]), float(line.split()[1])]
        GPS_data.append(record)

#Convert GPS data into a numpy array and perform clustering on it
X = np.array(GPS_data)
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
cluster_labels=kmeans.labels_


#merge cluster labels with their respective GPS coordinates
cluster_labels=cluster_labels.reshape(-1,1)
GPS_cluster_info=np.hstack([X,cluster_labels])


cluster1_points=[]
#store  points belonging to cluster 1 cluster1_points=[]
for index in range(len(GPS_cluster_info)):
    if GPS_cluster_info[index][2] == 0:
        cluster1_points.append(GPS_cluster_info[index])

np.save('cluster1',np.array(cluster1_points))
print(np.shape(np.array(cluster1_points)))

cluster2_points = []
# store  points belonging to cluster 1 cluster1_points=[]
for index in range(len(GPS_cluster_info)):
    if GPS_cluster_info[index][2] == 1:
        cluster2_points.append(GPS_cluster_info[index])

np.save('cluster2',np.array(cluster2_points))
print(np.shape(np.array(cluster2_points)))



#convert numpy array to 2D list and associate color red with cluster '0' and color blue with cluster '1'
GPS_cluster_info=GPS_cluster_info.tolist()
for index in range(len(GPS_cluster_info)):
    if GPS_cluster_info[index][2] == 0:
        GPS_cluster_info[index] += ['blue']
    else:
        GPS_cluster_info[index] += ['red']

