from oar import trainer

#print('Hello World!')
Trainer = trainer.Trainer('')
#print(Trainer.parse_corpus("I want to make America great again... Don't you think so? Huh!|p|t"))
print(Trainer.Classifier.show_most_informative_features(10))