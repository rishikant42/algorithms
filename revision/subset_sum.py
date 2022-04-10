wt = [3, 34, 4, 12, 5, 2]
W = 9

n = len(wt)


def knapsack(W, wt, n):
    if W == 0:
        return True

    if n == 0:
        return False

    if wt[n-1] > W:
        return knapsack(W, wt, n-1)

    return knapsack(W-wt[n-1], wt, n-1) or \
        knapsack(W, wt, n-1)


print(knapsack(W, wt, n))
