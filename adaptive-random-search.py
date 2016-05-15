from random import randrange

def objective_function(vector):
    return sum(x ** 2 for x in vector)
    
def rand_in_bounds(min, max):
    return randrange(min, max)
  
def random_vector(minmax):
