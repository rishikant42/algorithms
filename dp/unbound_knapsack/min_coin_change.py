import sys

coins = [1, 2, 5, 10]
target = 25
n = len(coins)


def knapsack(target, coins, n):
    if target == 0:
        return 0
    if n == 0:
        return float('inf')
    if coins[n-1] > target:
        return knapsack(target, coins, n-1)

    return min(
        1+knapsack(target-coins[n-1], coins, n),
        knapsack(target, coins, n-1)
    )

print(knapsack(target, coins, n))
