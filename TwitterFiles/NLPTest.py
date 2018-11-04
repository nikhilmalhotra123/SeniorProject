from __future__ import absolute_import
from __future__ import print_function
from nltk.corpus import stopwords
import nltk
import rake
import io
import re

# c = MailCreation()
# w = MailWriter()
# c.get_tweets()
# c.get_additonal_tweets()
# w.write_to_file()

__author__ = 'a_medelyan'

file = open("/Users/nikhilmalhotra/Desktop/NLPTest.txt", 'r+')
tweets = file.read().split("\n")

#'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
# "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself',
#  'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her',
# 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them',
# 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
# 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were',
# 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
# 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because',
# 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
# 'against', 'between', 'into', 'through', 'during', 'before', 'after',
# 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off',
# 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there',
# 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
# 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
# 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will',
# 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll',
# 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't",
# 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't",
# 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',
# "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
# 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


#
# for tweet in tweets:
#     temp = []
#     thing = nltk.word_tokenize(tweet)
#     if "https" in thing:
#         x = thing.index("https")
#         for i in [1,2,3]:
#             del thing[x]
#     thing = nltk.pos_tag(thing)
#     noun_verb = []
#     for word, tag in thing:
#         word = word.lower()  # in case they are not all lower cased
#         if word not in stopwords.words("english") and word != '’' and word != ',' and word != '\'s':
#             temp.append((word, tag))
#     if len(temp) > 10:
#         tweet = temp
#         for word, tag in tweet:
#             if tag[0:1] == "N" or tag[0:1] == "V":
#                 noun_verb.append((word, tag))
#     else:
#         tweets.remove(tweet)
#     noun_verb = []

thing = ['']
for tweet in tweets:
    pos = tweets.index(tweet)
    tweets[pos] = re.sub(r'http\S+', '', tweet)
    # start = 0
    # for i in [1-10]:
    #     loc = tweet.find("https", start)
    #     if tweet.find(" ", loc) > 0:
    #         tweets[pos] = tweet[:loc] + tweet[tweet.find(" ", loc):]
    #     else:
    #         tweets[pos] = tweet[:loc]
    #     start = loc
    if len(tweets[pos].split(" ")) >= 10:
        thing.append(tweets[pos])
stoppath = "/Users/nikhilmalhotra/TwitterEmailProject/RAKE-tutorial/data/stoplists/SmartStoplist.txt"
rake_object = rake.Rake(stoppath, 5, 3, 1)
for tweet in thing:
    try:
        print(type(tweet))
        keywords = rake_object.run(tweet)
        if (len(keywords[0][0].split(" ")) < 2):
            print(keywords[0][0] + " " + keywords[1][0])
        else:
            print(keywords[0][0])
        print("\n----------\n")
    except:
        pass
