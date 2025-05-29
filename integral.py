import math
import matplotlib.pyplot as plt
import numpy as np
import time

def evaluate_function(func, x):
    try:
        y = eval(func, {"np": np, "x": x})
        return y
    except Exception as e:
        print(f"Error in function evaluation: {e}")
        return None

def evaluate_lower(a):
    try:
        ea = eval(a,{"np":np})
        return ea
    except Exception as e:
        print(f"Error in lower bound evaluation:{e}")
        return None

def evaluate_upper(b):
    try:
        eb = eval(b,{"np":np})
        return eb
    except Exception as e:
        print(f"Error in upper bound evaluation:{e}")
        return None

func = input("function(e.g. np.sin(x), x**2):")
dx = int(input("dx:"))
if dx < 0:
    print("dx must be greater than 0")
    dx = int(input("dx:"))

a = input("lower bound:")
a1 = evaluate_lower(a)
b = input("upper bound:") 
b1 = evaluate_upper(b)
x = np.linspace(a1,b1,dx)
y = evaluate_function(func, x)

start_time = time.time()

for _ in range(10 ** 6):
    pass

if y is not None:
    deltax = (b1 - a1) / dx
    vals = y * deltax
    print(sum(vals))
else:
    print("Invalid function input.")

end_time = time.time()
print(f"Execution time: {end_time - start_time:.5f} seconds")


