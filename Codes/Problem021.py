import time
start = time.time()

def remove_duplicates(l):
    # Removes duplicate values of the given list
    return list(set(l))

def sum_divisors(num):
    divisors = [1]
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(int(num / i))
    return sum(remove_duplicates(divisors))

def is_amicable_number(a):
    b = sum_divisors(a)
    if a == sum_divisors(b):
        if a != b:
            return True
    return False

limit = 10000
sum_of_all_amicable_numbers = 0
for i in range(2,limit):
    if is_amicable_number(i):
        sum_of_all_amicable_numbers += i

print("sum of all amicable numbers under",limit,"is",sum_of_all_amicable_numbers)

print("it took {} seconds".format(time.time() - start))
