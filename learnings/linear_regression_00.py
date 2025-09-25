#!/home/glacroix/Documents/linear_regression/venv/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

X = df.values[:, :-1]

Y = df.values[:, -1]

fit = LinearRegression().fit(X, Y)

m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

plt.plot(X, Y, 'o') # scatterplot
plt.plot(X, m*X+b) # line
plt.show()