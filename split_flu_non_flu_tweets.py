#partition the tweets related to flu and not related to flu as two reparate files
flu_ptr=open('extracted_flu_non_flu_tweets/flu_examples.txt','w')
non_flu_ptr=open('extracted_flu_non_flu_tweets/non_flu_examples.txt','w')
flu_ptr_bag=open('extracted_flu_non_flu_tweets/flu_examples_bag_of_words.txt','w')
non_flu_ptr_bag=open('extracted_flu_non_flu_tweets/non_flu_examples_bag_of_words.txt','w')
with open("extracted_flu_non_flu_tweets/flu_non_flu_tweets.txt", 'r') as f:
    for line in f:
        if(line.split('\t')[1].replace('\n','') == 'flu'):
            flu_ptr.write(line)
            flu_ptr_bag.write(line.split('\t')[0])
        else:
            non_flu_ptr.write(line)
            non_flu_ptr_bag.write(line.split('\t')[0])
flu_ptr.close()
non_flu_ptr.close()
flu_ptr_bag.close()
non_flu_ptr_bag.close()
