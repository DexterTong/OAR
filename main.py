import pickle
import os
from oar import trainer

save_dir = 'temp/'            # Where to save classifier, extractor, etc
nbc_fn = 'classifier'               # What to save the Naive Bayes Classifier as
ext_fn = 'extractor'                # Filename of saved extractor

if os.path.exists(save_dir + nbc_fn + '.pkl') and os.path.exists(save_dir + ext_fn + '.pkl'):
    saved_nbc = open(save_dir + nbc_fn + '.pkl', 'rb')
    classifier = pickle.load(saved_nbc)
    saved_nbc.close()
    saved_ext = open(save_dir + ext_fn + '.pkl', 'rb')
    extractor = pickle.load(saved_ext)
    saved_ext.close()
else:
    Trainer = trainer.Trainer('')
    classifier = Trainer.Classifier
    extractor = Trainer.Extractor
    os.makedirs(save_dir)
    saved_nbc = open(save_dir + nbc_fn + '.pkl', 'wb')
    pickle.dump(classifier, saved_nbc, -1)
    saved_nbc.close()
    saved_ext = open(save_dir + ext_fn + '.pkl', 'wb')
    pickle.dump(extractor, saved_ext, -1)
    saved_ext.close()

#print(Trainer.parse_corpus("I want to make America great again... Don't you think so? Huh!|p|t"))
#print(Trainer.Classifier.show_most_informative_features(10))


test = "Good to hear it. Now, onward to victory!"
print(classifier.classify(extractor.ext_features(test.split())))
