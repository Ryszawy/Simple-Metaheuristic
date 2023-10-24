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


def rosenbrock(x):
    return sum(100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2 for i in range(len(x) - 1))


def supo(x):
    return sum(abs(i) ** (i + 1) for i in x)


def step(x):
    return sum((i + 0.5) ** 2 for i in x)

def cigar_function(x):
    s = sum([xi ** 2 for xi in x[1:]])
    s = s * 10e6
    a = x[0] ** 2
    return a + s


functions_array = [sphere_function, f2_function, schwefel_function, rosenbrock, supo, step, cigar_function]
functions_name = ["sphere_function", "f2_function", "schwefel_function", "rosenbrock", "supo", "step", "cigar_function"]
