def max_heap(a,i):
    l = 2*i+1
    r = 2*i+2
    s = len(a)

    if(l < s and a[i] <= a[l]):
        largest = l
    else:
        largest = i

    if(r < s and a[largest] <= a[r]):
        largest = r

    if(largest != i):
                
        a[i],a[largest] = a[largest],a[i]
        max_heap(a,largest)

def build_max(a):
    t = len(a)/2
    while(t>=0):
        max_heap(a,t)
        t = t-1
    return a

def heap_sort(a):
    x = []
    r = len(a)
    while(r > 0):
        k = build_max(a)
        x.append(k[0])
        a.remove(k[0])
        r = r-1
    
    print x
    

p = [1,14,10,8,7,9,3,2,4,6,6,45,25,78,98]
heap_sort(p)


##Note that it is not general heap sort method
##this heap sort algorithm work only in python
