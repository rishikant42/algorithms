def max_profit(price, n, k):
    profit = [[0 for i in range(n+1)] for j in range(k+1)]

    for i in range(1, k+1):
        prev_diff = float('-inf')
        for j in range(1, n):
            prev_diff = max(prev_diff, profit[i-1][j-1]-price[j-1])
            profit[i][j] = max(profit[i][j-1], price[j]+prev_diff)

    return profit[k][n-1]


k = 3
price = [12, 14, 17, 10, 14, 13, 12, 15]
n = len(price)

print(max_profit(price, n, k))
