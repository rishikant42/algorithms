s = "geeksforgeeks"
n = len(s)


def check_distinct(s, i, j):
    visited = []

    for k in range(i, j):
        if s[k] in visited:
            return False
        visited.append(s[k])
    return True


def lcs(s, n):
    res = 0
    for i in range(n):
        for j in range(i, n):
            if check_distinct(s, i, j):
                res = max(res, j-i+1)
    return res


print(lcs(s, n))
