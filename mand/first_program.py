#!/home/glacroix/Documents/linear_regression/venv/bin/python3

import sys
import pandas as pd


# TODO: the values are exploding, need to reduce learning rate
# TODO: current predicted price is false
def gradient_descent(mileage: float):
    points = list(pd.read_csv("../data.csv").itertuples())
    
    m = 0.0
    b = 0.0
    L = 0.00000001

    iterations = 100_000


    n = float(len(points))

    for i in range(iterations):
        # slope with respect to m
        D_m = sum(2 * p.km * ((m * p.km + b) - p.price) for p in points)

        # slope with respect to b
        D_b = sum(2 * ((m * p.km + b) - p.price) for p in points)
        m -= L * D_m
        b -= L * D_b

        if i % 10000 == 0:
            print(f"Iteration {i}: m={m}, b={b}, D_m={D_m}, D_b={D_b}")
        if abs(m) > 1e10 or abs(b) > 1e10:
            print("Values exploding! Reduce learning rate.")
            break

    print("y = {0}x + {1}".format(m, b))
    # print(f"The price of the car is {m * mileage + b} euros")


try: 
    mileage = float(input("How much mileage does your car have? "))

    if mileage < 0:
        print("Your car's mileage cannot be negative")
        sys.exit(1)

    gradient_descent(mileage)

    print(f"your car has {mileage} km")
except ValueError:
    print("Please input a valid number")
