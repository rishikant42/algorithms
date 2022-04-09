nums = [2, 3, 5, 6, 8, 10]

n = len(nums)

target = 10

def count_subset_sum(target, nums, n):
    if target == 0:
        return 1
    if n == 0:
        return 0

    if (nums[n-1] > target):
        return count_subset_sum(target, nums, n-1)

    return count_subset_sum(target-nums[n-1], nums, n-1) + count_subset_sum(target, nums, n-1)

print(count_subset_sum(target, nums, n))
