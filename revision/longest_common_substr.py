x = "abcdxyz"
y = "xyzabcd"

m = len(x)
n = len(y)


def lcs(x, y, m, n, count):
    if m == 0 or n == 0:
        return count

    if x[m-1] == y[n-1]:
        return lcs(x, y, m-1, n-1, count+1)

    return max(
        lcs(x, y, m-1, n, 0),
        lcs(x, y, m, n-1, 0),
    )


print(lcs(x, y, m, n, 0))
