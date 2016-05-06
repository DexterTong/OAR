

class Analyzer:

    def __init__(self):
        return

    def analyze(self, comments, classifier, extractor):
        pos = 0
        neg = 0
        for comment in comments:
            if classifier.classify(extractor.ext_features(comment)) == 'positive':
                pos += 1
                print('\033[92mpos: \033[0m', end='')
            else:
                neg += 1
                print('\033[91mneg: \033[0m', end='')
            print(' '.join(comment))
        print('Positive: ', pos, ' Negative: ', neg)
        return (pos, neg)
