# Randomize quick sort

import random 

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = random.choice(array)
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
    
        return sort(less) + equal + sort(greater)
    else:  
        return array


a=[12,4,5,6,7,3,1,15]

p = sort(a)
print p
