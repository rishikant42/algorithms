def max_heap(a,i):
    
    l = 2*i + 1
    r = 2*i + 2
    s = len(a)

    if(l<s and a[l] >= a[i]):
        largest = l
    else: largest = i

    if(r<s and a[r] >= a[largest]):
       largest = r

    if(a[i] != a[largest]):
        t = a[i]
        a[i] = a[largest]
        a[largest] = t

        print a
        max_heap(a,largest)
    


p = [1,14,10,8,7,9,3,2,4,6]

print p
max_heap(p,0)
