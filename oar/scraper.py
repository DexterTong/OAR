import praw
r = praw.Reddit(user_agent='opinion_analysis_for_reddit')
bernie = r.get_subreddit('sandersforpresident')
hillary = r.get_subreddit('hillaryclinton')

# Trump's subreddit is full of jokes ("memes") and doesn't look particularly useful
# donald = r.get_subreddit('the_donald')
# There is very little activity on the subreddits of the other candidates: Cruz, Rubio, Kasich, Stein, Johnson, etc

posts = hillary.get_hot(limit=10)
post = next(posts)
comments = praw.helpers.flatten_tree(post.comments)
for comment in comments:
    if comment.body.find('good') != -1:
        print('positive')
    else:
        print('negative')

print('done!')
