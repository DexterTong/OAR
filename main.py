import sys
from oar import trainer, scraper, analyzer, scorer

if len(sys.argv) == 3:
    training_corpus = sys.argv[1]
    test_corpus = sys.argv[2]
else:
    training_corpus = 'train_corpus'         # Default values
    test_corpus = 'test_corpus'

# 'all' for everything in ../corpora/ or '<corpus_name>' for a specific one
CE = trainer.Trainer().train_classifier(training_corpus)
classifier = CE[0]
extractor = CE[1]
Scraper = scraper.Scraper()
analyzer = analyzer.Analyzer()
scorer = scorer.Scorer()

#print(classifier.show_most_informative_features(50))
#print(classifier.classify(extractor.ext_features(test.split())))
#print(classifier._label_probdist.prob('positive'))
#comments = Scraper.scrape_comments('clinton', 1)

comments = Scraper.read_corpus(test_corpus, 0)
results = analyzer.analyze(comments, classifier, extractor)
#print(results)
scorer.score(results, test_corpus)
#print(classifier.show_most_informative_features(50))
