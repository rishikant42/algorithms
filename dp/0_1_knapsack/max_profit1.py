def knapsack(w, wt, val, n):
    if n == 0 or w == 0:
        return 0
    if wt[n-1] <= w:
        return max(
            val[n-1] + knapsack(w-wt[n-1], wt, val, n-1),
            knapsack(w, wt, val, n-1)
        )
    else:
        return knapsack(w, wt, val, n-1)


val = [60, 100, 120]
wt = [10, 20, 30]

W = 50
n = len(val)

print(knapsack(W, wt, val, n))
