# Annotation aid to make annotating stuff nice and easy
import praw
import sys

corp_dir = 'corpora'
test_dir = 'test'

if len(sys.argv) < 3:
    print('Usage: python3 annotator.py <submission ID> <destination>')
    quit(1)
f = open(corp_dir + '/' + sys.argv[2], 'x')     # If a FileExistsError pops up, pick a new filename
r = praw.Reddit(user_agent='opinion_analysis_for_reddit')
post = r.get_submission(submission_id=sys.argv[1])
comments = praw.helpers.flatten_tree(post.comments)
i = 1
pos = 0
neg = 0
dis = 0
hill = 0
bern = 0
for comment in comments:
    if hasattr(comment, 'body'):
        text = comment.body.replace('\n', '')
        print(text)
        tone = input('\033[92m' + str(i) +
                     ": Is this (1) positive or (2) negative? (3) to discard: \033[0m")
        if tone == '3':
            dis += 1
            continue
        if tone == '1':
            text += '\tpositive'
            pos += 1
        else:
            text += '\tnegative'
            neg += 1
        subj = input('\033[92m' + str(i) +
                     ": (4) Bernie or (5) Hillary? (6) to exit: \033[0m")
        if subj == '6':
            f.close()
            break
        if subj == '5':
            text += '\thillary\t\n'
            hill += 1
        else:
            text += '\tbernie\t\n'
            bern += 1
        f.write(text)
    else:  # If the comment object has no content, i.e. 'load more comments'
        continue
    i += 1
print('Positive: ', pos, ' Negative: ', neg, ' Discarded: ', dis, ' Bernie: ', bern, ' Hillary: ', hill)
f.close()
