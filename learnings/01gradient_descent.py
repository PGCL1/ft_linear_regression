#! /home/glacroix/Documents/linear_regression/venv/bin/python3

import random

def f(x):
    return (x - 3) ** 2 + 4

def dx_f(x):
    return 2*(x - 3)

# Learning Rate
L = 0.001

# iterations
iterations = 100_000

x = random.randint(-15, 15)

for i in range(iterations):

    # get slope
    d_x = dx_f(x)

    # update x by substracting the (learning rate * slope)
    x -= L * d_x

print(x, f(x))