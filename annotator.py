# Annotation aid to make annotating stuff nice and easy
import praw
import sys

corp_dir = 'corpora'

if len(sys.argv) < 3:
    print('Please provide 2 arguments: the submission ID of the post to scrape, and filename for new corpus')
    quit(1)
f = open(corp_dir + '/' + sys.argv[2], 'x')     # If a FileExistsError pops up, pick a new filename
r = praw.Reddit(user_agent='opinion_analysis_for_reddit')
post = r.get_submission(submission_id=sys.argv[1])
comments = praw.helpers.flatten_tree(post.comments)
i = 1
pos = 0
neg = 0
dis = 0
for comment in comments:
    if hasattr(comment, 'body'):
        text = comment.body.replace('\n', '')
        print(text)
        tone = input('\033[92m' + str(i) + ": Is this (1) positive or (2) negative? (3) to discard, (4) to exit: \033[0m")
        if tone == '4':
            f.close()
            break
        if tone == '3':
            dis += 1
            continue
        if tone == '1':
            text += '\tpositive\t\n'
            pos += 1
        else:
            text += '\tnegative\t\n'
            neg += 1
        f.write(text)
    else:  # If the comment object has no content, i.e. 'load more comments'
        continue
    i += 1
print('Positive: ', pos, ' Negative: ', neg, ' Discarded: ', dis)
f.close()
