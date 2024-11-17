def power(base, exponent):
    if exponent == 0:
        return 1
    temp = power(base, exponent // 2)
    if exponent % 2 == 0:
        return temp * temp
    else:
        return base * temp * temp

def compute(a, n):
    exponent = 1
    for i in range(n):
        exponent *= 2
    return power(a, exponent)
print(compute(3,3))