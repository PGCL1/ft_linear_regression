#!/home/glacroix/Documents/linear_regression/venv/bin/python3

import pandas as pd

points = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples()

m = 1.93939
b = 4.73333

sum_of_squares = 0.0

for p in points:
    y_actual = p.y
    y_predict = m * p.x + b
    residual_squared = (y_predict - y_actual)**2
    sum_of_squares += residual_squared

print("sum of squares = {}".format(sum_of_squares))