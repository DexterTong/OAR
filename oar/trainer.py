import nltk, string
from .extractor import Extractor

# Builds the classifier from training corpora


class Trainer:
    source = ''
    Extractor = None
    Classifier = None

    def __init__(self, source):
        Trainer.source = source
        Trainer.train_classifier(Trainer.source)
        return

    @staticmethod
    def parse_corpus(sentence):
        s1 = sentence.lower().split('|')
        s2 = s1[0].split()
        s3 = []
        for word in s2:
            s3.append(word.strip(string.punctuation))
        s1[0] = s3
        if len(s1) == 2:
            if 'p' in s1[1] | 'e' in s1[1] | 'n' in s1[1]:
                s1[2] = ''
            else:
                s1[2] = s1[1]
                s1[1] = ''
        s1[2] = s1[2].rstrip('\n')
        s3 = tuple(s1)
        return s3

    @staticmethod
    def get_words_in_comments(comment):
        all_words = []
        for words in comment:
            all_words.append(words)
        # print(all_words)
        return all_words

    @staticmethod
    def get_features(wordslist):
        wordslist = nltk.FreqDist(wordslist)
        wordfeatures = wordslist.keys()
        return wordfeatures

    @staticmethod
    def train_classifier(source):
        corpus = []
        if source == '':
            f = open('../corpora/hillary_train')
        else:
            f = open(source)
        for line in f:
            corpus.append(Trainer.parse_corpus(line))
        all_words = []
        for comment in corpus:
            new_words = Trainer.get_words_in_comments(comment[0])
            for word in new_words:
                all_words.append(word)
        word_features = Trainer.get_features(all_words)
        Trainer.Extractor = Extractor(word_features)
        training_set = nltk.classify.apply_features(Extractor.ext_features, corpus)
        #print(training_set)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        Trainer.Classifier = classifier
        return
