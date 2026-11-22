#!/usr/bin/env python3

import sys
import json

def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    return theta0 + theta1 * mileage


if __name__ == "__main__":
    try:
        with open("config.json", 'r', encoding='utf-8') as f:
            config_data = json.load(f)

        theta0 = float(config_data.get("theta0"))
        theta1 = float(config_data.get("theta1"))

    except FileNotFoundError:
        print("Config file not found! Using default values.")
        theta0, theta1 = 0, 0

    except json.JSONDecodeError:
        print("Invalid JSON format in config file! Using defaults.")
        theta0, theta1 = 0, 0

    try:
        mileage = float(input("How much mileage does your car have? "))

        if mileage < 0:
            print("Your car's mileage cannot be negative")
            sys.exit(1)

        price = estimate_price(mileage, theta0, theta1)
        print(f"The estimated price of your car is: {price}")

    except ValueError:
        print("Please input a valid number (enter 'q' to quit)")
        sys.exit(1)
