import numpy as np

def inc_array(x):
    # Location postion 1
    x[1] = x[1] + 1

def comp_array(x, y):
    if x[0] < y [0]:
        y = np.zeros(4) # This will create a new array of zero's and assign it to y.
    print(f"y is function, {y}")

a = np.array([0,1,2,3])
b = np.array([1,2,3,4])

inc_array(a)
comp_array(a, b)
print(f"a: {a}")
print(f"b: {b}")
