wt = [5, 10, 15]
val = [10, 30, 20]

W = 100
n = len(wt)


def knapsack(W, wt, val, n):
    if W == 0 or n == 0:
        return 0

    if (wt[n-1] > W):
        return knapsack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapsack(W-wt[n-1], wt, val, n),
            knapsack(W, wt, val, n-1)
        )


print(knapsack(W, wt, val, n))
