def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [4, 1, 5, 7, 2, 6, 3]
print(bubblesort(arr))

arr = [6, 1, 5, 1, 2, 6, 3]
print(bubblesort(arr))
