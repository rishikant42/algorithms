def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        print A
        max_heapify(A, largest)

def build_max_heap(A):
    i = len(A)/2
    while(i>=0):
        max_heapify(A,i)
        i = i-1

p = [1, 14, 10, 8, 7, 9, 3, 2, 4, 6]

print p

build_max_heap(p)

