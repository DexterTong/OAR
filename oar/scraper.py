import praw
import nltk
r = praw.Reddit(user_agent='opinion_analysis_for_reddit')
bernie = r.get_subreddit('sandersforpresident')
hillary = r.get_subreddit('hillaryclinton')

# Trump's subreddit is full of jokes (memes) and very little serious content
# donald = r.get_subreddit('the_donald')
# There is very little activity on the subreddits of the other candidates: Cruz, Rubio, Kasich, Stein, Johnson, etc


def parse_corpus(sentence):
    s1 = sentence.lower().split('|')
    s2 = s1[0].split()
    s1[0] = s2
    if len(s1) == 2:
        if 'p' in s1[1] | 'e' in s1[1] | 'n' in s1[1]:
            s1[2] = ''
        else:
            s1[2] = s1[1]
            s1[1] = ''
    s1[2] = s1[2].rstrip('\n')
    s3 = tuple(s1)
    return s3


def get_words_in_comments(comment):
    all = []
    for words in comment:
        all.append(words)
    #print(all)
    return all


def get_features(wordslist):
    wordslist = nltk.FreqDist(wordslist)
    wordfeatures = wordslist.keys()
    return wordfeatures


def ext_features(doc):
    doc_words = set(doc)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in doc_words)
    return features

i = 10
#posts = hillary.get_hot(limit = i)
corpus = []
f = open('../corpora/hillary_train')
for line in f:
    corpus.append(parse_corpus(line))

all_words = []
for comment in corpus:
    new_words = get_words_in_comments(comment[0])
    for word in new_words:
        all_words.append(word.rstrip('.'))
word_features = get_features(all_words)
#print(word_features)
#features = ext_features(['i', 'love', 'hillary'], word_features)
#print(features)

training_set = nltk.classify.apply_features(ext_features, corpus)
for line in training_set:
    print(line)

post = r.get_submission(submission_id='4gm30h')
for x in range(1, 2):
    #post = next(posts)
    comments = praw.helpers.flatten_tree(post.comments)
    n = 0;
    for comment in comments:
        content = (comment.body.replace('\'', '\\\'')).replace('\n', ' ')
        if len(content) < 20:
            continue
        if content.count('[deleted]') > 0:
            continue
        #print('\t(\'' + content + '\', \'\', \'\'),')
        n += 1
        #print(comment.score)
        #if hasattr(comment, 'body'):  # For now, ignore 'More Comments' objects, it takes too long to load them all
        #    if comment.body.find('x') != -1:
        #        print(comment.body)
        #    else:
        #        print(comment.body)
        #else:
        #    print('error')