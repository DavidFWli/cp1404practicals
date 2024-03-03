"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.175  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 1.0
days = 0
price = INITIAL_PRICE
print(f"${price:,.2f}")
with open('output.txt', 'w') as f:
    while MIN_PRICE <= price <= MAX_PRICE:
        price_change = 0
        random_int = random.randint(1, 2)
        days += 1
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print(f"On day {days} price is:${price:,.2f}")
        f.write(str(price) + '\n')

print("txt have been writen")
