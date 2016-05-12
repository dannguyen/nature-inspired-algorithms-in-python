---
source_url: http://cleveralgorithms.com/nature-inspired/stochastic/random_search.html
---

# Random search

~~~py
from random import random

def objective_function(vector):
    return sum(x ** 2 for x in vector)

def random_vector(minmax):
    vec = []
    for i in range(len(minmax)):
        a = minmax[i][0] + ((minmax[i][1] - minmax[i][0] * random()))
        vec.append(a)
    return a

def search(search_space, max_iter):
    best = None
    for i in max_iter do:
        candidate = {}
        candidate['vector'] = random_vector(search_space)
        candidate['cost'] = objective_function(candidate[:vector])
        if not best or candidate['cost'] < best['cost']:
            best = candidate
    return best
~~~



