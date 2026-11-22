#!/usr/bin/env python3

import sys
print(f"Python Path: {sys.executable}")
try:
    import pandas as pd
    print(f"✅ Pandas loaded! Version: {pd.__version__}")
except:
    print("❌ Import failed")
import matplotlib.pyplot as plt
import numpy as np
import json


def rescaling_values(rows: tuple):
    max_km = (max(col.km for col in rows))
    min_km = (min(col.km for col in rows))

    max_price = (max(col.price for col in rows))
    min_price = (min(col.price for col in rows))

    flattened_km = [(col.km - min_km)/(max_km - min_km) for col in rows]
    flattened_price = [(col.price - min_price)/(max_price - min_price) for col in rows]

    return (flattened_km, flattened_price, (min_km, max_km, min_price, max_price))


def calculate_cost(predictions, actual):
    """Calculate Mean Squared Error - this is the SQUARED cost function"""
    n = len(predictions)
    return sum((predictions[i] - actual[i])**2 for i in range(n)) / n


# TODO: add a line to show lossfunction
def show_data(theta1: float, theta0: float, info: tuple):
    points = pd.read_csv("data.csv")
    min_km, max_km, min_price, max_price = info

    # Unscale m and theta0
    theta1_unscaled = theta1 * (max_price - min_price) / (max_km - min_km)
    theta0_unscaled = theta0 * (max_price - min_price) + min_price - theta1_unscaled * min_km

    plt.scatter(points['km'], points['price'])
    plt.xlabel("Mileage in kms")
    plt.ylabel("Price in euros")
    plt.title('ScatterPlot of Car Prices per Mileage')

    x_line = np.sort(points['km'])
    y_line = theta1_unscaled * x_line + theta0_unscaled
    plt.plot(x_line, y_line, color='red', label='Regression Line')

    plt.legend()
    plt.show()


def gradient_descent(mileage: float):
    points = list(pd.read_csv("data.csv").itertuples())

    flattened_km, flattened_price, info = rescaling_values(points)
    min_km, max_km, min_price, max_price = info

    theta1 = 0.0
    theta0 = 0.0
    L = 0.1

    iterations = 100000
    n = len(points)

    for i in range(iterations):

        preds = [theta1*x + theta0 for x in flattened_km]

        # calculating square_loss also know as cost
        cost = calculate_cost(preds, flattened_price)

        D_theta1 = 1/2 * sum((preds[j] - flattened_price[j]) * flattened_km[j] for j in range(n))/n
        D_theta0 = 1/2 * sum((preds[j] - flattened_price[j]) for j in range(n)) / n

        # finding new values of theta1 and theta0 to reduce the loss function
        theta1 -= L * D_theta1
        theta0 -= L * D_theta0

        # Print progress
        if i % 10000 == 0 or i == iterations - 1:
            print(f"Iteration {i:4d}: Cost={cost:.10f}, theta1={theta1:8.4f}, theta0={theta0:8.4f}")
        # Safety check
        if abs(theta1) > 1e10 or abs(theta0) > 1e10:
            print("⚠️  Values exploding! Reduce learning rate.")
            break

    print("-" * 60)
    print(f"Final model: y = {theta1:.4f}x + {theta0:.4f}")
    print()

    mileage_scaled = (mileage - min_km) / (max_km - min_km)
    price_scaled = theta1 * mileage_scaled + theta0
    price_unscaled = price_scaled * (max_price - min_price) + min_price

    print(f"The price of the car is {price_unscaled} euros")
    return theta1, theta0, info


if __name__ == "__main__":
    try:
        mileage = float(input("How much mileage does your car have? "))

        if mileage < 0:
            print("Your car's mileage cannot be negative")
            sys.exit(1)

        theta1, theta0, info = gradient_descent(mileage)
        data = {"theta0": theta0, "theta1": theta1}
        with open('output.json', 'w') as f:
            json.dump(data, f)
        show_data(theta1, theta0, info)

    except ValueError:
        print("Please input a valid number")
