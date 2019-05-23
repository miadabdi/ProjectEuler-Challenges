from time import time
start = time()

def is_the_same(num, power):
    return num == sum([int(digit) ** power for digit in str(num)])

power = 5
result = [i for i in range(2, 6 * 9 ** 5) if is_the_same(i, power)]

print("sum: ", sum(result))
print("it took {} seconds".format(time() - start))

# One line solution :
# print(sum(i for i in range(2,6*9**5+1) if sum(int(n)**5 for n in str(i)) == i))
