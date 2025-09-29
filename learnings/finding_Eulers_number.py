#! /home/glacroix/Documents/linear_regression/venv/bin/python3

p = 1 # principal: starting amount

def compound_interest(interest_rate, time):
    return (1 + interest_rate / time) ** time

print(f" compound interest for 100 years {compound_interest(1, 100)}")
print(f" compound interest for 100 years {compound_interest(1, 1000)}")
print(f" compound interest for 100 years {compound_interest(1, 10000)}")
print(f" compound interest for 100 years {compound_interest(1, 100000)}")