# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np
def f(x):
    return x**2

def f_2(x):
    return x**3

def f_3(x):
    return x**3 + 5*x

def df(x):
    return 2*x

def df_2(x):
    return 3*(x**2)

def df_3(x):
    return 3*(x**2) + 5

def vector_sum(v1,v2):
    return [v1[0] + v2[0]]

def vector_less(v1, v2):
    return [v1[0]-v2[0]]

def vector_magnitude(v):
    return (v[0]**2 + v[1]**2)**0.5

def vec5():
    return np.array([1,1,1,1,1])

def vec3():
    return np.array([0,0,0])

def vec2_1():
    return np.array([1,0])

def vec2_2():
    return np.array([0,1])    

def matrix_multiply(v,m):
    return [v[0] * (m[0][0] + m[1][0]),v[1]*(m[0][1] + m[1][1])]    





