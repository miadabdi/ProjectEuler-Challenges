def divisor(num):
    divisors = 2 # Every number has 2 divisors at least. 1 and the number itself
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            divisors += 2
    return divisors

natural_number = 1
triangle_numbers = 1
while True:
    if divisor(triangle_numbers) > 500:
        print("The number is:",triangle_numbers)
        break
    natural_number += 1
    triangle_numbers += natural_number
