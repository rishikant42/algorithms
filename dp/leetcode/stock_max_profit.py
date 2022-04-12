def max_profit(prices, start, end):
    if start >= end:
        return 0

    profit = 0

    for i in range(start, end):
        for j in range(i+1, end+1):
            if prices[j] > prices[i]:
                curr_profit = prices[j] - prices[i] + max_profit(prices, start, i-1) + max_profit(prices, j+1, end)
                profit = max(curr_profit, profit)

    return profit


def max_profit2(prices, days):
    profit = 0

    for i in range(days-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]

    return profit


prices = [100, 180, 260, 310, 40, 535, 695]
n = len(prices)

# print(max_profit(prices, 0, n-1))
print(max_profit2(prices, n))
