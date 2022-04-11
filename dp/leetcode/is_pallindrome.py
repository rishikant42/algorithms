def reverse_str(s, n):
    if n == 0:
        return ""
    return s[n-1] + reverse_str(s, n-1)


def is_pallindrom1(s):
    if s == reverse_str(s, len(s)):
        return True
    return False


def is_pallindrome2(s):
    n = len(s) // 2
    for i in range(n):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

print(is_pallindrom1("malayalam"))
print(is_pallindrome2("malayalam"))
print(is_pallindrome2("abccba"))
