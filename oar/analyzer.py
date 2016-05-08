

class Analyzer:
    # These of course assume that the only 2 people worth discussing are these two
    bernonyms = {'bernie', 'bern', 'sanders', 'he', 'his', 'him', "he's", 'bernard', "bernie's", "sanders'"}
    hillonyms = {'hillary', 'rodham', 'clinton', 'hrc', 'her', 'she', 'hill', "she's", "hillary's", "clinton's"}

    def __init__(self):
        return

    def analyze(self, comments, classifier, extractor):
        h_pos = 0
        h_neg = 0
        b_pos = 0
        b_neg = 0
        o_pos = 0
        o_neg = 0
        results = []
        for comment in comments:
            subject = self.decide_subject(comment)
            if classifier.classify(extractor.ext_features(comment)) == 'positive':
                if subject is 'hill':
                    h_pos += 1
                    results.append(['positive', 'hillary'])
                elif subject is 'bern':
                    b_pos += 1
                    results.append(['positive', 'bernie'])
                else:
                    results.append(['positive', '?'])
                print('\033[92m', subject, ': \033[0m', end='')
            else:
                if subject is 'hill':
                    h_neg += 1
                    results.append(['negative', 'hillary'])
                elif subject is 'bern':
                    b_neg += 1
                    results.append(['negative', 'bernie'])
                else:
                    results.append(['negative', '?'])
                #print('\033[91m', subject, ': \033[0m', end='')
            #print(' '.join(comment))
        print('Hillary:\nPositive: ', h_pos, ' Negative: ', h_neg)
        print('Bernie:\nPositive: ', b_pos, ' Negative: ', b_neg)
        print('Total: ', h_pos+b_pos+h_neg+b_neg+o_pos+o_neg, 'Positive: ',
              h_pos+b_pos+o_pos, 'Negative: ', h_neg+b_neg+o_neg)
        return results

    def decide_subject(self, comment):
        bernie_count = 0
        hillary_count = 0
        for word in comment:
            if word in self.bernonyms:
                bernie_count += 1
            elif word in self.hillonyms:
                hillary_count += 1
        if hillary_count == bernie_count:
            return '?'
        if hillary_count > bernie_count:
            return 'hill'
        return 'bern'
