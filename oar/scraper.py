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
