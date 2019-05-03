import time
start = time.time()

def Fib_seq(limit):
    #returns numbers of Fib sequence under limit
    result = []
    a , b = 1 , 1
    while b < limit:
        a , b = b , a + b
        result.append(a)
    return result

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

sum_even_fib = 0
for item in Fib_seq(4000000):
    #generating list of Fib sequence
    if is_even(item):
        #checking be even
        sum_even_fib += item

print("Sum: {}".format(sum_even_fib))

end = time.time()
print("it took {} seconds".format(end - start))
