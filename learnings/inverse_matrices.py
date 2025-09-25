#! /home/glacroix/Documents/linear_regression/venv/bin/python3

import pandas as pd
from numpy.linalg import inv
import numpy as np

df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

X = df.values[:, :-1].flatten()

X_1 = np.vstack([X, np.ones(len(X))]).T

Y = df.values[:, -1]

b = inv(X_1.transpose() @ X_1) @ (X_1.transpose() @ Y)
print(b)

y_predict = X_1.dot(b)