mapping={
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_integer(roman):
    res = 0
    for i in range(len(roman)):
        if i + 1 < len(roman) and mapping[roman[i]] < mapping[roman[i+1]]:
            res -= mapping[roman[i]]
        else:
            res += mapping[roman[i]]
    return res

print(roman_to_integer("IV"))
