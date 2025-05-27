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

func = input("function(e.g. np.sin(x), x**2):")
dx = input("dx:")
if dx == None:
    dx = 10000


if dx < 0:
    print("dx must be greater than 0")
    dx = int(input("dx:"))

a = float(input("lower bound:"))
b = float(input("upper bound:")) 
x = np.linspace(a,b,dx)
y = evaluate_function(func, x)

start_time = time.time()


for _ in range(10 ** 6):
    pass

if y is not None:
    delx = (b - a) / dx
    vals = y * delx
    print(sum(vals))
else:
    print("Invalid function input.")

end_time = time.time()
print(f"Execution time: {end_time - start_time:.5f} seconds")

