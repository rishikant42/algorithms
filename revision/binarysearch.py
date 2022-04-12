def binary_search_recursive(arr, low, high, x):
    if low > high:
        return -1

    mid = (low+high) // 2

    mid_element = arr[mid]

    if mid_element < x:
        low = mid + 1
    elif mid_element > x:
        high = mid - 1
    else:
        return mid
    return binary_search_recursive(arr, low, high, x)


def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        mid_element = arr[mid]

        if mid_element < x:
            low = mid+1
        elif mid_element > x:
            high = mid-1
        else:
            return mid
    return -1


def binary_search_arr_split(arr, x):
    if not arr:
        return False
    mid = len(arr) // 2
    if arr[mid] < x:
        return binary_search_arr_split(arr[mid+1:], x)
    elif arr[mid] > x:
        return binary_search_arr_split(arr[:mid-1], x)
    return True


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search_recursive(arr, 0, 9, 8))
