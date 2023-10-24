import numpy as np

# range <-100; 100> ; dim 20/30 ; acc -> 0.0001
def sphere_function(x_array):
    return np.sum(np.power(x_array, 2))

# range <-100; 100> ; dim 20/30 ; acc -> 0.0001
def f2_function(x_array):
  temp = [x_array[i] - i for i in range(len(x_array))]
  return np.sum(np.power(temp, 2))

# range <-10; 10> ; 2 ; acc -> 0.000001
def schwefel_function(x_array):
    s1 = np.sum(np.power(np.absolute(x_array), 2))
    s2 = np.prod(np.absolute(x_array))
    return s1 + s2

functions_array = [sphere_function, f2_function, schwefel_function]

