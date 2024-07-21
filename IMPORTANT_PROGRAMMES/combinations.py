from time import monotonic
from random import randint, seed
from numpy import array
from math import prod

seed(0)
m = [randint(0, 400) for i in range(10_000_000)]

def get_combination1(comb, num):
    res = []
    for i in range(comb[0]):
        for j in range(prod(comb[1:])):
            res.append([i])
    for i, n in enumerate(comb[1:]):
        u = 0
        w = 0
        while u < len(res):
            if w > n - 1: w = 0
            for j in range(prod(comb[1:][i + 1:])):
                res[u].append(w)
                u += 1
            w += 1
    return res[num]

start_t = monotonic()
for i in range(prod(m)):
    get_combination1(m, i)
print(monotonic() - start_t)

