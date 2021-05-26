import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import nps_chat
nltk.download('nps_chat')
print(movie_reviews.fileids())
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
posts = nltk.corpus.nps_chat.xml_posts()[:10000]
random.shuffle(documents)
print("Zadanie 1\n")
all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

print((find_features(movie_reviews.words('pos/cv745_12773.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]

#train classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)
print("----------------------------------------------------------------")
print("Zadanie 2")

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features[format(word.lower())] = True
    return features

featuresets2 = [(dialogue_act_features(post.text),post.get('class')) for post in posts]
size = int(len(featuresets2) * 0.1)
train_set = featuresets2[size:]
test_set  = featuresets2[:size]

classifier2 = nltk.NaiveBayesClassifier.train(featuresets2)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier2,test_set))*100)
classifier2.show_most_informative_features(15)