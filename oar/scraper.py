import praw
from string import punctuation


class Scraper:
    r = None

    def __init__(self):
        self.r = praw.Reddit(user_agent='opinion_analysis_for_reddit')
        return

    def scrape_comments(self, sub, num):
        mode = 0
        if sub == 'sanders':
            subreddit = self.r.get_subreddit('sandersforpresident')  # Bernie Sanders
        elif sub == 'clinton':
            subreddit = self.r.get_subreddit('hillaryclinton')  # Hillary Clinton
        elif sub == 'trump':
            subreddit = self.r.get_subreddit('the_donald')  # Donald Trump, full of memes and trolling => Waste of time
        elif sub == 'politics':
            subreddit = self.r.get_subreddit('politics')  # Political discussion, pro-Bernie, anti-Hillary
        elif sub == 'politicaldiscussion':
            subreddit = self.r.get_subreddit('politicaldiscussion')  # Civil political discussion, somewhat pro-Hillary
        elif len(sub) == 6:
            mode = 1
        else:
            raise ValueError('Which subreddit do you want to scrape?')
            # Not enough people talk about the other candidates, remaining or not, to analyze anything
        if mode == 0:
            scraped_comments = []
            all_posts = subreddit.get_hot(limit=num)
            for post in all_posts:
                scraped_comments += self.scrape_helper(post)
        else:
            post = self.r.get_submission(submission_id=sub)
            scraped_comments = self.scrape_helper(post)
        return scraped_comments


    def scrape_helper(self, post):
        scraped_comments = []
        comments = praw.helpers.flatten_tree(post.comments)
        for comment in comments:
            if hasattr(comment, 'body'):
                com_pre = comment.body.lower().split()
                com_post = []
                for word in com_pre:
                    com_post.append(word.strip(punctuation))
                scraped_comments.append(com_post)
            else:  # If the comment object has no content, i.e. 'load more comments'
                continue
        return scraped_comments
