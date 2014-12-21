def merge(left,right):
    """Assumes left and right are sorted lists.
Returns a new sorted list containing the same elements
as (left + right) would contain."""
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while (i < len(left)):
        result.append(left[i])
        i = i + 1
    while (j < len(right)):
        result.append(right[j])
        j = j + 1
    return result

def mergesort(L):
    """Returns a new sorted list with the same elements as L"""
    print L
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) / 2
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
        together = merge(left,right)
        print 'merged', together
        return together

p = [8,2,4,9,3,6]
mergesort(p)
