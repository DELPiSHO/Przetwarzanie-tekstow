import nltk
from nltk.book import *
import re
from nltk.tokenize import RegexpTokenizer
import itertools
listOfAllTexts = [text1,text2,text3,text4,text5,text6,text7,text8,text9]
listOfAllSents = [sent1,sent2,sent3,sent4,sent5,sent6,sent7,sent8,sent9]
#zadanie1
print("---ZADANIE1------------------------------------")
text1.common_contexts(["Moby","Dick"])
text2.common_contexts(["I","here"])
text3.common_contexts(["stories","picktures"])
text4.common_contexts(["he","she"])
text5.common_contexts(["he","she"])
text6.common_contexts(["he","she"])
text7.common_contexts(["he","she"])
text8.common_contexts(["he","she"])
text9.common_contexts(["he","she"])
#zadanie2
print("---ZADANIE2------------------------------------")
zad2List = [["text1",len(text1),len(set(text1)),(len(text1)/len(set(text1))).__round__(2)],
            ["text2",len(text2),len(set(text2)),(len(text2)/len(set(text2))).__round__(2)],
            ["text3",len(text3),len(set(text3)),(len(text3)/len(set(text3))).__round__(2)],
            ["text4",len(text4),len(set(text4)),(len(text4)/len(set(text4))).__round__(2)],
            ["text5",len(text5),len(set(text5)),(len(text5)/len(set(text5))).__round__(2)]]
print("| tekst  | liczba slow | slowa rozne | lexical diversity |")
print("----------------------------------------------------------")
for item in zad2List:
    print("|",item[0]," "*(5-len(item[0])),"|",
    item[1]," "*(10-len(str(item[1]))),"|",
    item[2]," "*(10-len(str(item[2]))),"|",
    item[3]," "*(16-len(str(item[3]))),"|")
print("----------------------------------------------------------")
#zadanie3
print("---ZADANIE3------------------------------------")
zad3 = []
for word in text1:
    if(len(word) == 4 and word.isalpha()):
        zad3.append(word)
print(len(zad3))
print("---ZADANIE4------------------------------------")
big = []
for word in text5:
    if(len(word) > 17 and word.isalpha()):
        big.append(word)
print(big)
print("---ZADANIE5------------------------------------")
def slownik(zdanie):
    dictc = []
    res = []
    for word in zdanie:
        dictc.append(word)
    for word in zdanie:
        if word not in res:
            res.append(word)
    print(res)
slownik(sent1)
glowny_slownik = sent1  + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8 + sent9
glowny_slownik = set(glowny_slownik)
help = []
for word in glowny_slownik:
    if word.isalpha() or word.isdigit():
        word = word.lower()
        help.append(word)
help = sorted(set(help))
print(help)
print("---ZADANIE6------------------------------------")
def VocabSize(book):
    Slownik = []
    licznik = 0
    for word in book:
        if word in Slownik:
            continue
        else:
            Slownik.append(word.lower())
    for word in Slownik:
        licznik += 1
    print(licznik)
for book in listOfAllTexts:
    VocabSize(book)
print("---ZADANIE7------------------------------------")
cleanText = []
for word in text1:
    if word.isalpha():
        cleanText.append(word.lower())
comm = FreqDist(cleanText)
print(comm.most_common(10))
print("---ZADANIE8------------------------------------")
maxLen1 = max(len(word) for word in text1)
maxText1 = [word for word in text1 if (len(word) == maxLen1)]
print("Najdłuższe słowa w text1 to:")
print(maxText1)
maxLen2 = max(len(word) for word in text2)
maxText2 = [word for word in text2 if (len(word) == maxLen2)]
print("Najdłuższe słowa w text2 to:")
print(maxText2)
maxLen3 = max(len(word) for word in text3)
maxText3 = [word for word in text3 if (len(word) == maxLen3)]
print("Najdłuższe słowa w text3 to:")
print(maxText3)
maxLen4 = max(len(word) for word in text4)
maxText4 = [word for word in text4 if (len(word) == maxLen4)]
print("Najdłuższe słowa w text4 to:")
print(maxText4)
cleanText5 = []
for word in text5:
    word = re.sub(r'www.\S+','',word)
    word = re.sub(r'http\S+', '', word)
    cleanText5.append(word)
maxLen5 = max(len(word) for word in cleanText5)
maxText5 = [word for word in cleanText5 if (len(word) == maxLen5)]
print("Najdłuższe słowa w text5 to:")
print(maxText5)
maxLen6 = max(len(word) for word in text6)
maxText6 = [word for word in text6 if (len(word) == maxLen6)]
print("Najdłuższe słowa w text6 to:")
print(maxText6)