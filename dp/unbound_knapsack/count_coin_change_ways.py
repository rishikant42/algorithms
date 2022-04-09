coins = [1, 2, 3]
target = 5
n = len(coins)

def count_ways(target, coins, n):
    if target == 0:
        return 1
    if n == 0:
        return 0
    if coins[n-1] > target:
        return count_ways(target, coins, n-1)

    return count_ways(target, coins, n-1) + count_ways(target-coins[n-1], coins, n)


print(count_ways(target, coins, n))
