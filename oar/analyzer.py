

class Analyzer:
    # These of course assume that the only 2 people worth discussing are these two
    bernonyms = {'bernie', 'bern', 'sanders', 'he', 'his', 'him', "he's", 'bernard'}
    hillonyms = {'hillary', 'rodham', 'clinton', 'hrc', 'her', 'she', 'hill', "she's"}

    def __init__(self):
        return

    def analyze(self, comments, classifier, extractor):
        h_pos = 0
        h_neg = 0
        b_pos = 0
        b_neg = 0
        for comment in comments:
            subject = self.decide_subject(comment)
            if classifier.classify(extractor.ext_features(comment)) == 'positive':
                if subject is 'hill':
                    h_pos += 1
                elif subject is 'bern':
                    b_pos += 1
                else:
                    continue
                print('\033[92m', subject, ': \033[0m', end='')
            else:
                if subject is 'hill':
                    h_neg += 1
                elif subject is 'bern':
                    b_neg += 1
                else:
                    continue
                print('\033[91m', subject, ': \033[0m', end='')
            print(' '.join(comment))
        print('Hillary:\nPositive: ', h_pos, ' Negative: ', h_neg)
        print('Bernie:\nPositive: ', b_pos, ' Negative: ', b_neg)
        print('Total: ', h_pos+b_pos+h_neg+b_neg, 'Positive: ', h_pos+b_pos, 'Negative: ', h_neg+b_neg)
        return h_pos, h_neg, b_pos, b_neg

    def decide_subject(self, comment):
        bernie_count = 0
        hillary_count = 0
        for word in comment:
            if word in self.bernonyms:
                bernie_count += 1
            elif word in self.hillonyms:
                hillary_count += 1
        if hillary_count == bernie_count:
            return 'n'
        if hillary_count > bernie_count:
            return 'hill'
        return 'bern'
