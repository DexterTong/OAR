import sys
from oar import trainer, scraper, analyzer, scorer

if len(sys.argv) == 3:
    training_corpus = sys.argv[1]
    test_corpus = sys.argv[2]
else:
    training_corpus = 'train_corpus'         # Default values
    test_corpus = 'test_corpus'

# 'all' for everything in ../corpora/ or '<corpus_name>' for a specific one

# CE = trainer.Trainer().train_classifier('reddit', training_corpus)
# CE = trainer.Trainer().train_classifier('tweet', 'testdata.manual.2009.06.14.csv')
CE = trainer.Trainer().train_classifier('both', 'testdata.manual.2009.06.14.csv', training_corpus)
classifier = CE[0]
extractor = CE[1]
Scraper = scraper.Scraper()
analyzer = analyzer.Analyzer()
scorer = scorer.Scorer()

comments = Scraper.read_corpus(test_corpus, 0)
results = analyzer.analyze(comments, classifier, extractor)
scorer.score(results, test_corpus)
print(classifier.show_most_informative_features(10))
#print(classifier._label_probdist.prob('positive'))

