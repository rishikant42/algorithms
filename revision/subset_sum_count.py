wt = [3, 34, 12, 5, 9]
W = 9

n = len(wt)


def knapsack(W, wt, n):
    if W == 0:
        return 1

    if n == 0:
        return 0

    if wt[n-1] > W:
        return knapsack(W, wt, n-1)

    return knapsack(W-wt[n-1], wt, n-1) + knapsack(W, wt, n-1)


print(knapsack(W, wt, n))
