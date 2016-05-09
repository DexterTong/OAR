f = open('test_corpus', 'r')
nf = open('test_corpus3', 'w')
i = 0
for line in f:
    lines = line.split('\t')
    print(len(lines))
    #for i in range(0, 63):

    # parts = line.split('\t')
    # print(parts[0] + '\t' + parts[1])
    # subject = input('\033[92m' + str(i) + ": Is this (1) Bernie or (2) Hillary? (3) to discard: \033[0m")
    # if subject == '1':
    #     parts[2] = 'bernie'
    # elif subject == '2':
    #     parts[2] = 'hillary'
    # else:
    #     continue
    # new_text = parts[0] + '\t' + parts[1] + '\t' + parts[2]
    # nf.write(new_text)
    # i += 1
f.close()
nf.close()
