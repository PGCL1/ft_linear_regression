#!/Users/pgcl/Documents/DEV/outerCore/ft_linear_regression/venv/bin/python3

import pandas as pd

# import points from CSV
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

# building the model
m = 0.0
b = 0.0

# learning rate
L = 0.001

# the number of iterations
iterations = 100_000

n = float(len(points)) # number of elements in X

# perform gradient descent
for i in range(iterations):

    # slope with respect to m
    D_m = sum(2 * p.x * ((m * p.x + b) - p.y) for p in points)

    # slope with respect to b
    D_b = sum(2 * ((m * p.x + b) - p.y) for p in points)

    m -= L * D_m
    b -= L * D_b
    print("y = {0}x + {1}".format(m, b))

print("y = {0}x + {1}".format(m, b))
