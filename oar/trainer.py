import nltk
from string import punctuation
import os
from .extractor import Extractor

# Builds the classifier from training corpora


class Trainer:
    source = ''
    Extractor = None
    Classifier = None

    def __init__(self, source):
        self.source = source
        return

    @staticmethod
    def parse_corpus(sentence):
        s1 = sentence.lower().split('\t')
        s2 = s1[0].split()
        s3 = []
        for word in s2:
            s3.append(word.strip(punctuation))
        s1[0] = s3
        # if len(s1) == 2:
        #     if 'positive' in s1[1] or 'negative' in s1[1]:
        #         s1[2] = ''
        #     else:
        #         s1[2] = s1[1]
        #         s1[1] = ''
        # s1[2] = s1[2].rstrip('\n')
        s1[1] = s1[1].rstrip('\n')
        s3 = tuple(s1)
        return s3

    @staticmethod
    def get_words_in_comments(comment):
        all_words = []
        for words in comment:
            all_words.append(words)
        return all_words

    @staticmethod
    def get_features(wordslist):
        wordslist = nltk.FreqDist(wordslist)
        wordfeatures = wordslist.keys()
        return wordfeatures

    @staticmethod
    def train_classifier(source):
        corpus = []
        if source == 'all':
            for filename in os.listdir('../corpora'):
                if filename != 'about' and filename != 'editor.py':
                    f = open('../corpora/' + filename)
                    for line in f:
                        corpus.append(Trainer.parse_corpus(line))
                    f.close()
        else:
            if source == '':
                f = open('../corpora/hillary1')
                print("Using corpora/hillary1")
            else:
                f = open('../corpora/' + source)
                print("Using corpora/" + source)
            for line in f:
                corpus.append(Trainer.parse_corpus(line))
            f.close()
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
        return (classifier, Extractor)
