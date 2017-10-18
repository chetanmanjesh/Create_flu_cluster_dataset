import tweepy
import re
import time
import numpy as np
from sklearn.cluster import KMeans
consumer_key = '0uuMA9XJJhyeAsR97i6KE5jMz'
consumer_secret = 'onpeZ9f8A5uIhM2yXH2akmIk3YbgZF6QN8HvYSeBcbgR2iGDPF'
access_key = '919929307706920960-baqYTtlQFlSx5RdM7yR9XrAlVNRMO75'
access_secret = 'ZYj2fQpmHFjKt5NxXCGoFVM1ViarQI6AHeyvhrdCORyen'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

b=[]

regex = re.compile(r"((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?")


GPS_data=[]
with open('GPS_data/GPS_data.txt','r') as f:
    for line in f:
        record=[float(line.split()[0]), float(line.split()[1])]
        GPS_data.append(record)
        #print(record)
print(GPS_data)

count=0
flu_gps_comb=[]
with open("flu_non_flu_tweets.txt", 'r') as f:
    for line in f:
        if(count>=len(GPS_data)):
            print("more lines that datapoints")
            break
        combined_record= [line.split('\t')[i].replace('\n','') for i in range(0,len(line.split('\t')))]+GPS_data[count]
        flu_gps_comb.append(combined_record)
        print(combined_record)
        count+=1

X = np.array(GPS_data)
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
cluster_labels=kmeans.labels_


cluster_labels=cluster_labels.reshape(-1,1)

print(np.shape(cluster_labels))

'''
liste=[cluster_labels[i,0] for i in range(len(cluster_labels))]
print("Winston")
print(np.shape(liste))

if((liste==kmeans.labels_).all()):
    print('Halleluija')
'''

#for i in range(len(cluster_labels)):
   #print(cluster_labels[i])

GPS_cluster_info=np.hstack([X,cluster_labels])


#convert numpy array to 2D list

GPS_cluster_info=GPS_cluster_info.tolist()

for index in range(len(GPS_cluster_info)):
    if GPS_cluster_info[index][2] == 0:
        GPS_cluster_info[index] += ['blue']
    else:
        GPS_cluster_info[index] += ['red']

print(GPS_cluster_info)


#a1[0].text # Prints the message

