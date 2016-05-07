# Silly little script to edit corpora formats as necessary
# Only use/modify as necessary, and don't overwrite other corpora!

f = open('hillary2', 'r')
nf = open('hillary2', 'w')
i = 0
line2 = ''
for line in f:
    if i == 0:
        line2 = line.rstrip() + '\t'
        i += 1
    else:
        i = 0
        nf.write(line2 + line.lstrip())
nf.close()
