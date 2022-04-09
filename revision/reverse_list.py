def reverse_list(arr):
    if not arr:
        return []
    return [arr.pop()] + reverse_list(arr)


def reverse_fun(arr):
    if len(arr) == 1:
        return arr
    return reverse_fun(arr[1:]) + arr[0:1]


def reverse_fun2(arr):
    if len(arr) == 1:
        return arr
    return [arr[-1]] + reverse_fun(arr[:-1])


arr = [1, 2, 3, 4, 5]

# print(reverse_list(arr))
print(reverse_fun2(arr))
