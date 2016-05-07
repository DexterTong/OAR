from . import analyzer


class Scorer:
    Analyzer = None

    def __init__(self):
        self.Analyzer = analyzer.Analyzer()
        return

    def score(self, results, corpus):
        f = open('../test/' + corpus, 'rt')
        i = 0
        res = [[0]*6 for j in range(4)]
        for line in f:
            col = 0
            row = 0
            split_line = line.split('\t')
            tone = split_line[1]
            subject = split_line[2]
            #print(subject == 'bernie')
            if subject == 'bernie':
                row = 2
            if tone == 'negative':
                row += 1
            if results[i][1] == 'bernie':
                col = 2
            elif results[i][1] == '?':
                col = 4
            if results[i][0] == 'negative':
                col += 1
            #print(row, ' ', col)
            res[row][col] += 1
            i += 1
        f.close()
        print('        H+     H-     B+     B-     ?+     ?-  Total\n', end='')
        for j in range(0, 4):
            if j == 0:
                print('H+ ', end='')
            elif j == 1:
                print('H- ', end='')
            elif j == 2:
                print('B+ ', end='')
            else:
                print('B- ', end='')
            total = 0
            for k in range(0, 6):
                print('{:>7}'.format(res[j][k]), end='')
                total += res[j][k]
            print('{:>7}'.format(total))
        print('Tot', end='')
        for l in range(0, 6):
            col_total = 0
            for m in range(0, 4):
                col_total += res[m][l]
            print('{:>7}'.format(col_total), end='')
        return res
