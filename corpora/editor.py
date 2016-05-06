# Silly little script to edit corpora formats as necessary
# Only use/modify as necessary, and don't overwrite other corpora!

f = open('hillary1', 'r')
nf = open('hillary2', 'w')
for line in f:
    if line.find('\te') != -1:
        pass
    else:
        nf.write(line)
nf.close()
