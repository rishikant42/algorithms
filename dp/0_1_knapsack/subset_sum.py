nums = [3, 5, 7, 1, 6, 9, 2]

n = len(nums)

target = 34

def subset_sum(target, nums, n):
    if target == 0:
        return True
    if n == 0:
        return False

    if (nums[n-1] > target):
        return subset_sum(target, nums, n-1)

    return subset_sum(target-nums[n-1], nums, n-1) or subset_sum(target, nums, n-1)

print(subset_sum(target, nums, n))
