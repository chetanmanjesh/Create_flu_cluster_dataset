from sklearn.feature_extraction.text import CountVectorizer

#read the flu teets (directly related to personal sickness) and fit the read data using CountVectorizer
with open('extracted_flu_non_flu_tweets/flu_examples_bag_of_words.txt','r') as f:
    str=f.read()
    vectorizer = CountVectorizer(stop_words='english').fit([str]) #remove stop words in english

#get words and counts in document
word_counts = vectorizer.fit_transform([str]).toarray()[0]
words = vectorizer.get_feature_names()

#pair the words with their word counts as tuples
words_counts=list(zip(words,word_counts))


#sort the tuples in decreasing order of word count
words_counts.sort(key=lambda x : x[1])

words_counts.reverse()

#print the results
print("The top 20 words related to flu-tweets directly realted to personal sickness\n")

for i in range(0,21):
    print(words_counts[i][0])


from sklearn.feature_extraction.text import CountVectorizer

#read the teets (NOT directly related to personal sickness) and fit the read data using CountVectorizer
with open('extracted_flu_non_flu_tweets/non_flu_examples_bag_of_words.txt','r') as f:
    str=f.read()
    vectorizer = CountVectorizer(stop_words='english').fit([str]) #remove stop words in english

#get words and counts in document
word_counts = vectorizer.fit_transform([str]).toarray()[0]
words = vectorizer.get_feature_names()

#pair the words with their word counts as tuples
words_counts=list(zip(words,word_counts))


#sort the tuples in decreasing order of word count
words_counts.sort(key=lambda x : x[1])

words_counts.reverse()

#print the results
print("The top 20 words related to flu-tweets NOT directly realted to personal sickness\n")

for i in range(0,21):
    print(words_counts[i][0])