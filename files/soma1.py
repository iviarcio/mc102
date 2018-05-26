import sys


def soma(nCols, fileName):
    sums = [0] * nCols
    for line in open(fileName):
        cols = line.split()
        for i in range(nCols):
            sums[i] += eval(cols[i])
    return sums


print(soma(eval(sys.argv[1]), sys.argv[2]))
