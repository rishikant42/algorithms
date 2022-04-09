val = [60, 100, 120]
wt = [10, 20, 30]

W = 50
n = len(val)

# [[len of w]]   ==> len of n
# t[n][w]

t = [[-1 for i in range(W+1)] for j in range(n+1)]


def knapsack(w, wt, val, n):
    if n == 0 or w == 0:
        return 0
    if t[n][w] != -1:
        return t[n][w]
    if wt[n-1] <= w:
        t[n][w] = max(
            val[n-1] + knapsack(w-wt[n-1], wt, val, n-1),
            knapsack(w, wt, val, n-1)
        )
        return t[n][w]
    else:
        t[n][w] = knapsack(w, wt, val, n-1)
        return t[n][w]


print(knapsack(W, wt, val, n))
