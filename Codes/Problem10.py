import time
start = time.time()

def is_prime(num):
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return False
    return True

prime_numbers = [2]
for i in range(3,2000000,2):
    if is_prime(i):
        prime_numbers.append(i)
print("the sum of prime numbers =",sum(prime_numbers))

end = time.time()
print("it took {} seconds".format(end - start))
