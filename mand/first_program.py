#!/Users/pgcl/Documents/DEV/outerCore/ft_linear_regression/venv/bin/python3

import sys


def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    return theta0 + theta1 * mileage


try:
    theta0 = 0
    theta1 = 0
    mileage = float(input("How much mileage does your car have? "))

    if mileage < 0:
        print("Your car's mileage cannot be negative")
        sys.exit(1)

    price = estimate_price(mileage, theta0, theta1)
    print(f"The estimated price of your car is: {price}")

except ValueError:
    print("Please input a valid number")
