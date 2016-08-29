def msort(l):
    print l
    if len(l) < 2:
        return l
    else:
        mid = len(l) / 2
        left = msort(l[:mid])
        right = msort(l[mid:])

        together = merge(left, right)
        print "Merged ", together
    return together

def merge(l, r):
    i, j = 0, 0
    res = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    while i < len(l):
        res.append(l[i])
        i += 1

    while j < len(r):
        res.append(r[j])
        j += 1
    return res


x = [3, 4, 1, 2, 8, 6, 5, 7]
msort(x)
