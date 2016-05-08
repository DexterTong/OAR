# Silly little script to edit corpora formats as necessary
# Only use/modify as necessary, and don't overwrite other corpora!
import os, random


lines = open('all', 'r').readlines()
random.shuffle(lines)
train = open('train_corpus', 'wt')
test = open('../test/test_corpus', 'wt')
i = 0
for line in lines:
    if i == 7:
        i = 0
    if i == 0:
        test.write(line)
    else:
        train.write(line)
    i += 1
test.close()
train.close()