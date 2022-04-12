divisors=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
mapping={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}

result=[]


def integer_to_roman(num):
    res = ""
    if num in divisors:
        res = res + mapping[num]
        rem = 0
    else:
        for divisor in divisors:
            if divisor < num:
                quo = num // divisor
                rem = num % divisor
                res = res + mapping[divisor] * quo
                break

    result.append(res)
    if rem != 0:
        integer_to_roman(rem)

integer_to_roman(3549)

print(result)
