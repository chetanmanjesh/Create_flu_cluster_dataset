import numpy as np
#load the points belonging to each cluster
cluster_flu=np.load('cluster_data/cluster1.npy')
cluster_non_flu=np.load('cluster_data/cluster2.npy')

#associate an arbitary flu-tweet related to personal illness with an arbitrary point in cluster 1
#write record to file (record contains tweet, coordinates of tweet and cluster number)
count=0
flu_gps_comb=[]
f_write=open('merged_flu_cluster_records/flu_cluster.txt','w')
with open("extracted_flu_non_flu_tweets/flu_examples.txt", 'r') as f_read:
    for line in f_read:
        if(count >= len(cluster_flu)):
            print("more flu-tweets that datapoints")
            break
        combined_record = [line.split('\t')[0]] + cluster_flu[count].tolist()
        flu_gps_comb.append(combined_record)
        new_record='\t'.join(str(e) for e in combined_record)+'\n'
        f_write.write(new_record)
        print('....')
        print(new_record)
        print('....')

        count += 1


#associate an arbitary flu-tweet NOT related to personal illness with an arbitrary point in cluster 2
#write record to file (record contains tweet, coordinates of tweet and cluster number)
count=0
flu_gps_comb=[]
f_write=open('merged_flu_cluster_records/non_flu_cluster.txt','w')
with open("extracted_flu_non_flu_tweets/non_flu_examples.txt", 'r') as f_read:
    for line in f_read:
        if(count >= len(cluster_non_flu)):
            print("more non-flu tweets that datapoints")
            break
        combined_record = [line.split('\t')[0]] + cluster_non_flu[count].tolist()
        flu_gps_comb.append(combined_record)
        new_record='\t'.join(str(e) for e in combined_record)+'\n'
        f_write.write(new_record)
        print('....')
        print(new_record)
        print('....')

        count += 1
