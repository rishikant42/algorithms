coins = [2, 5, 3, 6]
target = 10

n = len(coins)


def knapsack(target, coins, n):
    if target == 0:
        return 1
    if n == 0:
        return 0

    if coins[n-1] > target:
        return knapsack(target, coins, n-1)

    return knapsack(target - coins[n-1], coins, n) + knapsack(target, coins, n-1)


print(knapsack(target, coins, n))
