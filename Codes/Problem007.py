import time
start = time.time()

def prime_number(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

counter_primes = 1
for num in range(3, 100000000, 2):
    if prime_number(num):
        counter_primes += 1
        if counter_primes == 10001:
            print("the 10001st prime number is:",num)
            break

end = time.time()
print("it took {} seconds".format(end - start))
