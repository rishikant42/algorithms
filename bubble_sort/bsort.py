def bubble_sort(a):
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if len(a) > j+1 and a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        #print a
    return a

a = [4, 6, 3, 7, 2, 5, 8, 1]
print bubble_sort(a)
