#Code to extract GPS data from file and perform clustering on it.
import numpy as np
from sklearn.cluster import KMeans



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


#convert numpy array to 2D list and associate color red with cluster '0' and color blue with cluster '1'
GPS_cluster_info=GPS_cluster_info.tolist()
for index in range(len(GPS_cluster_info)):
    if GPS_cluster_info[index][2] == 0:
        GPS_cluster_info[index] += ['blue']
    else:
        GPS_cluster_info[index] += ['red']



cluster1_points=[]
#store  points belonging to cluster 1 cluster1_points=[]
for index in range(len(GPS_cluster_info)):
    if GPS_cluster_info[index][2] == 0:
        cluster1_points.append(GPS_cluster_info[index])


print(cluster1_points)

cluster2_points = []
# store  points belonging to cluster 1 cluster1_points=[]
for index in range(len(GPS_cluster_info)):
    if GPS_cluster_info[index][2] == 1:
        cluster2_points.append(GPS_cluster_info[index])

print(cluster2_points)



#arbitrarily assign cluster points to tweets by merging one tweet with one cluster 'GPS' record obtained in the previous step
count=0
flu_gps_comb=[]
with open("flu_annotations/flu_non_flu_tweets.txt", 'r') as f:
    for line in f:
        if(count >= len(GPS_cluster_info)):
            print("more lines that datapoints")
            break
        combined_record = [line.split('\t')[i].replace('\n','') for i in range(0,len(line.split('\t')))]+GPS_cluster_info[count]
        flu_gps_comb.append(combined_record)
        print('....')
        #print(combined_record)
        print('....')
        count += 1