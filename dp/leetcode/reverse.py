def reverse_arr(arr, n):
    if n == 0:
        return []
    return [arr[n-1]] + reverse_arr(arr, n-1)


def reverse_arr2(arr):
    if not arr:
        return []
    return [arr.pop()] + reverse_arr2(arr)


def reverse_str(s, n):
    if n == 0:
        return ""
    return s[n-1] + reverse_str(s, n-1)


arr = [1, 2, 3, 4, 5]
s = "hello"
print(reverse_arr(arr, 5))
print(reverse_arr2(arr))
print(reverse_str(s, 5))
