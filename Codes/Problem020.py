def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact

number = 100
print("the sum of digits:",sum(int(digit) for digit in str(factorial(number))))
