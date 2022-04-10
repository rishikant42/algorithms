nums = [1, 5, 11, 5, 4]

n = len(nums)


def knapsack(W, nums, n):
    if W == 0:
        return True

    if n == 0:
        return False

    if nums[n-1] > W:
        return knapsack(W, nums, n-1)

    return knapsack(W-nums[n-1], nums, n-1) or \
        knapsack(W, nums, n-1)


def eq_partiton(nums, n):
    if sum(nums) % 2 != 0:
        return False
    W = sum(nums) / 2
    return knapsack(W, nums, n)


print(eq_partiton(nums, n))
