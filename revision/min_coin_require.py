import sys

coins = [25, 10, 5]
target = 30
n = len(coins)


def knapsack(target, coins, n):
    if target == 0:
        return 0
    if n == 0:
        return sys.maxsize + 1

    if coins[n-1] > target:
        return knapsack(target, coins, n-1)

    return min(
        1+knapsack(target-coins[n-1], coins, n),
        knapsack(target, coins, n-1)
    )


print(knapsack(target, coins, n))
