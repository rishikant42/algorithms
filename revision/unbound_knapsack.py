wt = [1, 50]
val = [1, 30]

W = 100
n = len(wt)

# t[n][W]
# t = [[-1 for j in range(W+1)] for i in range(n+1)]

t = []
for i in range(n+1):
    x = []
    for j in range(W+1):
        x.append(-1)
    t.append(x)


def knapsack(W, wt, val, n):
    if W == 0 or n == 0:
        return 0

    if t[n][W] != -1:
        return t[n][W]

    if wt[n-1] > W:
        t[n][W] = knapsack(W, wt, val, n-1)
        return t[n][W]

    t[n][W] = max(
        val[n-1] + knapsack(W-wt[n-1], wt, val, n),
        knapsack(W, wt, val, n-1)
    )
    return t[n][W]


print(knapsack(W, wt, val, n))
