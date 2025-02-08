import numpy as np

def big_cal(x):
    a = 1
    b = 1
    result = a/x + 1
    return result

a = np.array(range(1,100))
a[72] = 0

for i in a:
    temp = big_cal(int(i)) # Using break point condition, i.e. when the value of i is equal to 72
    print(f"temp for value {i}  in {temp}")