def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0

    if wt[n-1] > W:
        return knapsack(wt, val, W, n-1)

    return max(
        val[n-1] + knapsack(wt, val, W-wt[n-1], n-1),
        knapsack(wt, val, W, n-1)
    )


val = [60, 100, 120]
wt = [10, 20, 30]

W = 50
n = len(val)

print(knapsack(wt, val, W, n))
