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

def reverse_str(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_str(s[:-1])


def reverse_str2(s):
    if len(s) == 1:
        return s
    return reverse_str2(s[1:]) + s[0:1]


def reverse_arr(arr, n):
    if n == 0:
        return []

    return [arr[n-1]] + reverse_arr(arr, n-1)

def reverse_str3(s, n):
    if n == 0:
        return ""

    return s[n-1] + reverse_str3(s, n-1)




arr = [1, 2, 3, 4, 5]

# print(reverse_list(arr))
# print(reverse_fun2(arr))
print(reverse_arr(arr, 5))
print(reverse_str("hello"))
print(reverse_str2("hello"))
print(reverse_str3("hello", 5))
