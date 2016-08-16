import sys

def isort(a):
    l = len(a)
    for j in range(1, l):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
    return a

num = map(int, sys.argv[1:])
print isort(num)
