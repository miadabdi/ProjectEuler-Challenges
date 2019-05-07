import time
start = time.time()

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = 2 ** 1000
print("sum of the digits:",sum_of_digits(num))

end = time.time()
print("it took {} seconds".format(end - start))
