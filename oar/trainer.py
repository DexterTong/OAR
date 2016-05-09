import nltk
from string import punctuation
import string
from .extractor import Extractor
from nltk.corpus import stopwords

# Builds the classifier from training corpora


class Trainer:

    def __init__(self):
        return

    @staticmethod
    def parse_corpus(sentence):
        s1 = sentence.lower().split('\t')
        s2 = s1[0].split()
        s3 = []
        for word in s2:
            temp = word.strip(punctuation)
            #if temp not in stopwords.words('english'):
            s3.append(temp)
        s1[0] = s3
        s1[1] = s1[1].rstrip('\n')
        s3 = tuple(s1)
        return s3

    @staticmethod
    def parse_corpus_tweet(tweet):
        parts = tweet.split(',', 5)
        #for part in parts:
        #    part = part.strip(punctuation)
        text = parts[5].replace('@', '').split()
        parsed = [[], '']
        for word in text:
            temp = word.strip(punctuation).lower()
            #if temp not in stopwords.words('english'):
            parsed[0].append(temp)
        if parts[0] == '"0"':
            parsed[1] = 'negative'
            return tuple(parsed)
        if parts[0] == '"4"':
            parsed[1] = 'positive'
            return tuple(parsed)
        return None


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
    def train_classifier(mode, source, source2 = ''):
        corpus = []
        # if source == 'all':
        #     for filename in os.listdir('../corpora'):
        #         if filename != 'about' and filename != 'editor.py':
        #             f = open('../corpora/' + filename)
        #             for line in f:
        #                 corpus.append(Trainer.parse_corpus(line))
        #             f.close()
        # else:
        #     if source == '':
        #         f = open('../corpora/hillary1')
        #         print("Using corpora/hillary1")
        #     else:
        #         f = open('../corpora/' + source)
        #         print("Using corpora/" + source)
        #     for line in f:
        #         corpus.append(Trainer.parse_corpus(line))
        #     f.close()
        f = open('../corpora/' + source)
        if mode == 'tweet':
            for line in f:
                corpus.append(Trainer.parse_corpus_tweet(line))
        elif mode == 'reddit':
            for line in f:
                corpus.append(Trainer.parse_corpus(line))
        elif mode == 'both':
            i = 0
            for line in f:
                temp = Trainer.parse_corpus_tweet(line)
                if temp is not None:
                    corpus.append(temp)
            f.close()
            f = open('../corpora/' + source2)
            for line in f:
                corpus.append(Trainer.parse_corpus(line))
        else:
            quit(1)
        f.close()
        all_words = []
        for comment in corpus:
            new_words = Trainer.get_words_in_comments(comment[0])
            for word in new_words:
                all_words.append(word)
        word_features = Trainer.get_features(all_words)
        Trainer.Extractor = Extractor(word_features)
        training_set = nltk.classify.apply_features(Extractor.ext_features, corpus)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        return classifier, Extractor
