import nltk
from nltk.book import *
import re
import numpy as np
import matplotlib.pyplot as plt
from nltk import ngrams
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk import collections
from nltk.corpus import stopwords
from itertools import chain
from re import findall
from nltk.corpus import brown
listOfAllTexts = [text1,text2,text3,text4,text5,text6,text7,text8,text9]
listOfAllSents = [sent1,sent2,sent3,sent4,sent5,sent6,sent7,sent8,sent9]
print("---ZADANIE1------------------------------------")
cleanText = []
for word in text5:
    if word.isalpha():
        cleanText.append(word.lower())
comm = FreqDist(cleanText)
print(comm.most_common(10))
different_bigrams = list(set(bigrams(text5)))
print(len(different_bigrams))
diff_bigrams = FreqDist(different_bigrams)
print(diff_bigrams.most_common(10))
print("---ZADANIE2------------------------------------")
def get_each_ngrams(input_list, n,count = 0):
    for s in chain(*[get_ngrams(input_list,n)]):
        yield ' '.join(s)
        count += 1
    print(count)
    count = 0
def get_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])
for s in get_each_ngrams(text5,3):
    continue
for s in get_each_ngrams(text5,4):
    continue
for s in get_each_ngrams(text5,5):
    continue
for s in get_each_ngrams(text5,6):
    continue
print("---ZADANIE3------------------------------------")
n3 = 45008
n4 = 45007
n5 = 45006
n6 = 45005
x = np.arange(4)
plt.scatter([3,4,5,6],[45005,45006,45007,45008])
plt.legend()
plt.show()

print("---ZADANIE4------------------------------------(a)")
ing = []
for n in text1:
    if (n.endswith('ing') == True):
        ing.append(n)
print(ing)
print("---ZADANIE4------------------------------------(b)")
vowels = "aeiou"
totalCount = 0
for n in text2:
    wovelCount = len(findall("[%s]" % vowels,n))
    totalCount += wovelCount
print(totalCount)
print("---ZADANIE4------------------------------------(c)")
skrot = "U.S.A"
occ = text4.count(skrot)
print(occ)
print("---ZADANIE5------------------------------------")
def words_percentage(text):
    stop_words = set(stopwords.words('english'))
    without_stopwords = []
    allLen = len(text)
    count = 0
    count_without_sw = 0
    for n in text:
        count += 1
    for n in text:
        if n not in stop_words:
            count_without_sw += 1
    print("All words in text is " + str(count))
    print("Stopwords in text is " + str(count_without_sw))
    result = count_without_sw * 100/count
    print("Percentage of words without stopwords is " +"%.2f%%" % result)

i = 1
for text in listOfAllTexts:
    print("Text" + str(i))
    words_percentage(text)
    i += 1
print("---ZADANIE6------------------------------------")
def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1, w2, w3)
for tagged_sent in brown.tagged_sents():
        process(tagged_sent)