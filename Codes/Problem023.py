import time
start = time.time()

def divisors(num):
    result = [1]
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            result.append(i)
            result.append(num // i)
    return list(set(result))

def is_abundant_number(num):
    return sum(divisors(num)) > num

abundant_numbers = []
for num in range(1,28124):
    if is_abundant_number(num):
        abundant_numbers.append(num)

num = [0] * 28123
for i in range(0,len(abundant_numbers)):
    for j in range(i,len(abundant_numbers)):
        sum_abundant = abundant_numbers[i] + abundant_numbers[j]
        if sum_abundant < 28123:
            if num[sum_abundant] == 0:
                num[sum_abundant] = sum_abundant

print("the sum of numbers that cannot be produced by sum of two Abundant numbers is:", sum([index for index, i in enumerate(num) if i == 0]))

print("it took {} seconds".format(time.time() - start))
