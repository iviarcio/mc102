import sys


def soma(nCols, fileName):
    sums = [0] * nCols
    for line in open(fileName):
        cols = line.split(',')
        nums = [int(x) for x in cols]
        both = zip(sums, nums)
        sums = [x + y for (x, y) in both]
    return sums


print(soma(eval(sys.argv[1]), sys.argv[2]))
