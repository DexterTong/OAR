import praw


class Scraper:
    r = None

    def __init__(self):
        self.r = praw.Reddit(user_agent='opinion_analysis_for_reddit')
        return

    @staticmethod
    def scrape_comments(self, sub, mode, num):
        if sub == 'sanders':
            subreddit = self.r.get_subreddit('sandersforpresident')  # Bernie Sanders
        elif sub == 'clinton':
            subreddit = self.r.get_subreddit('hillaryclinton')  # Hillary Clinton
        elif sub == 'trump':
            subreddit = self.r.get_subreddit('the_donald')  # Donald Trump, full of memes and trolling => Waste of time
        elif sub == 'politics':
            subreddit = self.r.get_subreddit('politics')  # Political discussion, pro-Bernie, anti-Hillary
        elif sub == 'politicaldiscussion':
            subreddit = self.r.get_subreddit('politicaldiscussion')  # Civil political discussion, seems rather neutral
        else:
            raise ValueError('Which subreddit do you want to scrape?')
            # Not enough people talk about the other candidates, remaining or not, to analyze anything
        if mode == 1:
            all_posts = subreddit.get_hot(limit=num)
            for post in all_posts:
                comments = praw.helpers.flatten_tree(post.comments)
                for comment in comments:
                    if hasattr(comment, 'body'):
                        continue
                    else:  # If the comment object has no content, i.e. 'load more comments'
                        continue
        elif mode == 2:
            pass
        else:
            raise ValueError('Which mode? 1 = grab from posts, 2 = grab comments directly')

    # @staticmethod
    # def train_classifier(self, corpus):
    #     corpus = []
    #     f = open('../corpora/hillary_train')
    #     for line in f:
    #         corpus.append(parse_corpus(line))
    #     all_words = []
    #     for comment in corpus:
    #         new_words = get_words_in_comments(comment[0])
    #         for word in new_words:
    #             all_words.append(word.rstrip('.'))
    #     word_features = get_features(all_words)
    #     training_set = nltk.classify.apply_features(ext_features, corpus)
    #     # classifier = nltk.NaiveBayesClassifier(training_set)
    #     # for line in training_set:
    #     #    print(line)



    # posts = hillary.get_hot(limit = i)
    # post = r.get_submission(submission_id='4gm30h')
    # for x in range(1, 2):
    # post = next(posts)
    # comments = praw.helpers.flatten_tree(post.comments)
    # n = 0;
    # for comment in comments:
    #        content = (comment.body.replace('\'', '\\\'')).replace('\n', ' ')
    #        if len(content) < 20:
    #            continue
    #        if content.count('[deleted]') > 0:
    #            continue
    # print('\t(\'' + content + '\', \'\', \'\'),')
    #        n += 1
    # print(comment.score)
    # if hasattr(comment, 'body'):  # For now, ignore 'More Comments' objects, it takes too long to load them all
    #    if comment.body.find('x') != -1:
    #        print(comment.body)
    #    else:
    #        print(comment.body)
    # else:
    #    print('error')

    # @staticmethod
    # def parse_corpus(self, sentence):
    #     s1 = sentence.lower().split('|')
    #     s2 = s1[0].split()
    #     s1[0] = s2
    #     if len(s1) == 2:
    #         if 'p' in s1[1] | 'e' in s1[1] | 'n' in s1[1]:
    #             s1[2] = ''
    #         else:
    #             s1[2] = s1[1]
    #             s1[1] = ''
    #     s1[2] = s1[2].rstrip('\n')
    #     s3 = tuple(s1)
    #     return s3
    #
    # @staticmethod
    # def get_words_in_comments(self, comment):
    #     all_words = []
    #     for words in comment:
    #         all_words.append(words)
    #     # print(all_words)
    #     return all_words
    #
    # @staticmethod
    # def get_features(self, wordslist):
    #     wordslist = nltk.FreqDist(wordslist)
    #     wordfeatures = wordslist.keys()
    #     return wordfeatures
    #
    # @staticmethod
    # def ext_features(self, doc):
    #     doc_words = set(doc)
    #     features = {}
    #     for word in word_features:
    #         features['contains(%s)' % word] = (word in doc_words)
    #     return features
