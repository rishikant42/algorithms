def bsearch(s, e, first, last, calls):
    print first, last, calls
    if (last - first) < 2: return s[first] == e or s[last] == e
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid - 1, calls+1)
    else:return bsearch(s, e, mid + 1, last, calls + 1)

def search(s, e):
    print bsearch(s, e, 0, len(s) - 1, 1)

def sort(a):
    for j in range(1,len(a)):
        key = a[j]
        i = j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    return a

p = [5,4,1,3,2,6,8,13,25,78,65]
t = sort(p)

search(t,78)

#Element must give in sorted oder for using binary search
