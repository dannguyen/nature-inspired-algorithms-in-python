---
source_url: http://cleveralgorithms.com/nature-inspired/stochastic/random_search.html
---

# Random search

~~~py
from random import random
import numpy as np

def objective_function(vector):
    """
    >>> objective_function(np.array(2, 5))
    29
    """
    return sum(x ** 2 for x in vector)

def random_vector(minmax):
    """returns a vector...?????"""
    vec = []
    for i in range(len(minmax)):
        a = minmax[i][0] + ((minmax[i][1] - minmax[i][0] * random()))
        vec.append(a)
    return np.array(vec)

def search(search_space, max_iter):
    best = None
    for i in range(max_iter):
        candidate = {}
        candidate['vector'] = random_vector(search_space)
        candidate['cost'] = objective_function(candidate['vector'])
        if not best or candidate['cost'] < best['cost']:
            best = candidate
    return best


if __name__ == '__main__':
    problem_size = 2
    search_space = np.array([(-5, +5) for i in range(problem_size)])
    # algorithm configuration
    max_iter = 100
    best = search(search_space, max_iter)
    print("Done. Best solution: c={0}, v={1}".format(best['cost'], best['vector']))
# Done. Best solution: c=0.09250645875964783, v=[ 0.23871714  0.18846906]
~~~



