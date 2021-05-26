import nltk
from nltk.book import *
from nltk.corpus import *
from nltk import FreqDist
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet as swn

listOfAllTexts = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

print("---------ZADANIE1-----------------")
print(gutenberg.fileids())
print("---------ZADANIE2-----------------")
print(inaugural.fileids())
print("---------ZADANIE3-----------------")
print(movie_reviews.categories())
print("---------ZADANIE4-----------------")
print(inaugural.sents('1909-Taft.txt'))
print("---------ZADANIE5-----------------")
length = 0
adv = brown.words(categories = 'adventure')
advLen = len(adv)
for word in adv:
    if (word == 'mountains' or word == 'ocean' or word == 'Bungee jump'):
        length += 1
result = length * 100 / advLen
print(length)
print("Częstość występowania wydzielonych słów w kategorii adventure " +"%.3f%%" % result)
print("---------ZADANIE6-----------------")
inag = inaugural.words()
fdist = FreqDist(inag)
top_ten = fdist.most_common(10)
print(top_ten)
print("---------ZADANIE7-----------------")
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
print("---------ZADANIE8-----------------")
journalist = swn.senti_synset('journalist.n.01')
writer = swn.senti_synset('writer.n.01')
actor = swn.senti_synset('actor.n.01')
singer = swn.senti_synset('singer.n.01')
print(journalist)
print(writer)
print(actor)
print(singer)