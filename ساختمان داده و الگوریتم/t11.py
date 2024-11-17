def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        temp = power(base, exponent // 2)
        if exponent % 2 == 0:
            return temp * temp
        else:
            return base * temp * temp

a = int(input("Enter the first three-digit number: "))
b = int(input("Enter the second three-digit number: "))

product = a * b
first_digit = int(str(product)[0])
last_digit = product % 10

result = power(first_digit, last_digit)

print("The result is:", result)
