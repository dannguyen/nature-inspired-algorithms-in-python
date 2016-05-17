from random import randrange

def objective_function(vector):
    return sum(x ** 2 for x in vector)
    
def random_vector(minmax):
    return [randrange(minmax[i][0], minmax[i][1]) for i in range(len(minmax))]
    
def take_step(minmax, current, step_size):
    arr = []
    for i in len(current):
        _min = max([minmax[i][0], current[i] - step_size])
        _max = min([minmax[i][1], current[i] + step_size])
        arr[i] = randrange(_min, _max)
    return arr
