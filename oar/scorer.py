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
        print('Results Matrix: Actual tag in row, system tag in column')
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
        print('\nCandidate Tagging: Actual in row, system tag in column')
        print('       H      B      ?\nH', end='')
        hill_true = 0
        for i in range(0, 2):
            for j in range(0, 2):
                hill_true += res[j][i]
        print('{:>7}'.format(hill_true), end='')
        bern_false = 0
        for i in range(2, 4):
            for j in range(0, 2):
                bern_false += res[j][i]
        print('{:>7}'.format(bern_false), end='')
        hill_unk = 0
        for i in range(4, 6):
            for j in range(0, 2):
                hill_unk += res[j][i]
        print('{:>7}'.format(hill_unk), end='')
        print('\nB', end='')
        hill_false = 0
        for i in range(0, 2):
            for j in range(2, 4):
                hill_false += res[j][i]
        print('{:>7}'.format(hill_false), end='')
        bern_true = 0
        for i in range(2, 4):
            for j in range(2, 4):
                bern_true += res[j][i]
        print('{:>7}'.format(bern_true), end='')
        bern_unk = 0
        for i in range(4, 6):
            for j in range(2, 4):
                bern_unk += res[j][i]
        print('{:>7}'.format(bern_unk), end='')
        print('\nCorrect Ratio: ', (hill_true+bern_true)/(hill_true+bern_true+hill_false+bern_false+hill_unk+bern_unk))
        print('Incorrect Ratio: ',
              (hill_false+bern_false)/(hill_true+bern_true+hill_false+bern_false+hill_unk+bern_unk))
        print('Indeterminate Ratio: ',
              (hill_unk+bern_unk)/(hill_true+bern_true+hill_false+bern_false+hill_unk+bern_unk))
        return res
