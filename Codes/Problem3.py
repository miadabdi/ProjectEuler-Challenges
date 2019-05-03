def is_prime(num):
    #if the argument is prime returns "True"
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_factor(num):
    #Return a list of prime factors of the argument
    prime_factors = []
    for i in range(3,int(num ** 0.5)+1,2):
        if num % i == 0:
            if is_prime(i):
                prime_factors.append(i)
                if is_prime(num / i):
                    prime_factors.append(num / i)
    return prime_factors 

print("The largest prime factor is:", int(max(prime_factor(600851475143))))
