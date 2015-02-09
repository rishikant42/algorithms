def sort(a):
    for j in range(1,len(a)):
        print p
        key = a[j]
        i = j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    print p
p = [8,2,4,9,3,6]
sort(p)
     
