# Extract features from a comment


class Extractor:
    word_features = []

    def __init__(self, wf):
        Extractor.word_features = wf
        return

    @staticmethod
    def ext_features(doc):
        doc_words = set(doc)
        features = {}
        for word in Extractor.word_features:
            features['contains(%s)' % word] = (word in doc_words)
        print(features)
        return features
