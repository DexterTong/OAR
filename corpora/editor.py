# Silly little script to edit corpora formats as necessary
# Only use/modify as necessary, and don't overwrite other corpora!
import os, random, sys


# lines = open('all', 'r').readlines()
# random.shuffle(lines)
# train = open('train_corpus', 'wt')
# test = open('../test/test_corpus', 'wt')
# i = 0
# for line in lines:
#     if i == 7:
#         i = 0
#     if i == 0:
#         test.write(line)
#     else:
#         train.write(line)
#     i += 1
# test.close()
# train.close()

file = open(sys.argv[1], 'r')
pos = 0
neg = 0
for line in file:
    text = line.split('\t')
    if text[1].find('p') != -1:
        pos += 1
    else:
        neg += 1
file.close()
print('pos: ', pos, ' neg: ', neg)