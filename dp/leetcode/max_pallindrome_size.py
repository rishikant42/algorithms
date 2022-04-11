s = "abccbahello"
n = len(s)


def check_pallindrome(s, i, j):
    s1 = s[i:j]
    return s1 == s1[::-1]


def longestPalSubstr(s):
    n = len(s)
    max_length = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            flag = 1
            if check_pallindrome(s, i, j):
                flag = 0
            if (flag != 0 and (j - i + 1) > max_length):
                start = i
                max_length = j - i + 1
    return max_length


print(longestPalSubstr(s))
