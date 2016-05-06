import pickle
import os
from oar import trainer, scraper, analyzer


#Trainer = trainer.Trainer('bernie1')
#Trainer = trainer.Trainer('all')
#classifier = Trainer.Classifier
#extractor = Trainer.Extractor

CE = trainer.Trainer('bernie1').train_classifier('bernie1')
classifier = CE[0]
extractor = CE[1]
Scraper = scraper.Scraper()
analyzer = analyzer.Analyzer()

#print(Trainer.parse_corpus("I want to make America great again... Don't you think so? Huh!|p|t"))
#print(classifier.show_most_informative_features(50))
#print(classifier.classify(extractor.ext_features(test.split())))
#print(classifier._label_probdist.prob('positive'))
#print(classifier._label_probdist.prob('negative'))

#comments = Scraper.scrape_comments('clinton', 1)
#comments = Scraper.scrape_comments('4euxj8', 1)
comments = Scraper.read_corpus('bernie1')
analyzer.analyze(comments, classifier, extractor)
# for comment in comments:
#     if classifier.classify(extractor.ext_features(comment)) == 'positive':
#         pos += 1
#     else:
#         neg += 1
# print('positive: ', pos, ' negative: ', neg)
#print(classifier.show_most_informative_features(50))
