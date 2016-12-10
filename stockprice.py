def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

print(get_max_profit([-20,-3, 100, -5, 0, 50]))