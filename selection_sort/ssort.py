def selectionsort(a):
    for i in range(len(a)):
        least = i
        for k in range(i + 1 , len(a)):
            if a[k] < a[least]:
                least = k
        #swap(a, least, i)
        a[least], a[i] = a[i], a[least]
    return a


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

a = [8, 2, 6, 7, 4, 3, 1, 5]

print selectionsort(a)
