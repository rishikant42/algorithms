def isort(a):
    for j in range(1,len(a)):
        key = a[j]
        i = j-1
        while i>=0 and a[i]>key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a
a = [8,2,7,9,3,6]
print isort(a)
            
