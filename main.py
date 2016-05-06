import pickle
import os
from oar import trainer, scraper


Trainer = trainer.Trainer('hillary_bernie1')
classifier = Trainer.Classifier
extractor = Trainer.Extractor
Scraper = scraper.Scraper()

#print(Trainer.parse_corpus("I want to make America great again... Don't you think so? Huh!|p|t"))
#print(classifier.show_most_informative_features(50))
#print(classifier.classify(extractor.ext_features(test.split())))
#print(classifier._label_probdist.prob('positive'))
#print(classifier._label_probdist.prob('negative'))

#comments = Scraper.scrape_comments('clinton', 1)
comments = Scraper.scrape_comments('4euxj8', 1)
i = 0
j = 0
for comment in comments:
    if classifier.classify(extractor.ext_features(comment)) == 'positive':
        i += 1
    else:
        j += 1
print('positive: ', i, ' negative: ', j)
