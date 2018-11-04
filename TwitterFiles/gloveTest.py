from gensim.models import KeyedVectors
from nltk.corpus import wordnet as wn
import textrank

# a = wn.synsets("good", pos="n")
# print (a)
#
# for b in a:
#     print (b.definition())
#
# synonyms = []
# antonyms = []
#
# for syn in a:
#     for l in syn.lemmas():
#         synonyms.append(l.name())
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
#
# print("Synonyms: ", set(synonyms))
# print("Antonyms: ", set(antonyms))
# file = "/Users/nikhilmalhotra/Downloads/GoogleNews-vectors-negative300.bin"
# model = KeyedVectors.load_word2vec_format(file, binary=True)
#
# result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
# print (result)

print(textrank.extract_key_phrases("There are numerous weaknesses with the bag of words model, especially when applied to natural language processing tasks, that graph ranking algorithms such as TextRank are able to address. "))