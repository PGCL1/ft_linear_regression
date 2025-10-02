#!/Users/pgcl/Documents/DEV/outerCore/ft_linear_regression/venv/bin/python3

import sys
import pandas as pd
import matplotlib.pyplot as plt


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
def show_data(m: float, b: float):
    points = pd.read_csv("data.csv")
    plt.scatter(points['price'], points['km'])
    plt.xlabel("Price in euros")
    plt.ylabel("Mileage in kms")
    plt.title('ScatterPlot of Car Prices per mileage')

    # plt.Line2D(m, m + b)
    plt.show()


def gradient_descent(mileage: float):
    points = list(pd.read_csv("data.csv").itertuples())

    flattened_km, flattened_price, info = rescaling_values(points)
    min_km, max_km, min_price, max_price = info

    m = 0.0
    b = 0.0
    L = 0.1

    iterations = 100000
    n = len(points)

    for i in range(iterations):

        preds = [m*x + b for x in flattened_km]

        # calculating square_loss also know as cost
        cost = calculate_cost(preds, flattened_price)

        D_m = 1/2 * sum((preds[j] - flattened_price[j]) * flattened_km[j] for j in range(n))/n
        D_b = 1/2 * sum((preds[j] - flattened_price[j]) for j in range(n)) / n

        # finding new values of m and b to reduce the loss function
        m -= L * D_m
        b -= L * D_b

        # Print progress
        if i % 10000 == 0 or i == iterations - 1:
            print(f"Iteration {i:4d}: Cost={cost:.10f}, m={m:8.4f}, b={b:8.4f}")
        # Safety check
        if abs(m) > 1e10 or abs(b) > 1e10:
            print("⚠️  Values exploding! Reduce learning rate.")
            break

    print("-" * 60)
    print(f"Final model: y = {m:.4f}x + {b:.4f}")
    print()

    mileage_scaled = (mileage - min_km) / (max_km - min_km)
    price_scaled = m * mileage_scaled + b
    price_unscaled = price_scaled * (max_price - min_price) + min_price

    print(f"The price of the car is {price_unscaled} euros")
    return m, b


try: 
    mileage = float(input("How much mileage does your car have? "))

    if mileage < 0:
        print("Your car's mileage cannot be negative")
        sys.exit(1)

    m, b = gradient_descent(mileage)
    show_data(m, b)

except ValueError:
    print("Please input a valid number")
