import praw
r = praw.Reddit(user_agent='opinion_analysis_for_reddit')
bernie = r.get_subreddit('sandersforpresident')
hillary = r.get_subreddit('hillaryclinton')

# Trump's subreddit is full of jokes (memes) and very little serious content
# donald = r.get_subreddit('the_donald')
# There is very little activity on the subreddits of the other candidates: Cruz, Rubio, Kasich, Stein, Johnson, etc

i = 10
#posts = hillary.get_hot(limit = i)
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
        print('\t(\'' + content + '\', \'\', \'\'),')
        n += 1
        #print(comment.score)
        #if hasattr(comment, 'body'):  # For now, ignore 'More Comments' objects, it takes too long to load them all
        #    if comment.body.find('x') != -1:
        #        print(comment.body)
        #    else:
        #        print(comment.body)
        #else:
        #    print('error')