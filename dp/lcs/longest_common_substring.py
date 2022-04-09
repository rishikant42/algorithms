x = 'AGGTABrishi'
y = 'agGTAbkant'

n = len(x)
m = len(y)

def lcsubstring(x, y, n, m, count):
    if n == 0 or m == 0:
        return count
    if x[n-1] == y[m-1]:
        count = lcsubstring(x, y, n-1, m-1, count+1)
    else:
        count = max(
            count,
            max(lcsubstring(x, y, n-1, m, 0),lcsubstring(x, y, n, m-1, 0))
        )
    return count

print(lcsubstring(x, y, n, m, 0))
