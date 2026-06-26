print("📈 Stock Portfolio Tracker")

portfolio = {}
total_value = 0

n = int(input("How many stocks do you own? "))

for i in range(n):
    print(f"\nStock {i+1}")

    stock_name = input("Enter stock name: ").upper()
    stock_price = float(input("Enter stock price: "))
    quantity = int(input("Enter quantity: "))

    value = stock_price * quantity

    portfolio[stock_name] = value
    total_value += value

print("\n========== PORTFOLIO SUMMARY ==========")

for stock, value in portfolio.items():
    print(stock, ":", value)

print("\n💰 Total Portfolio Value =", total_value)