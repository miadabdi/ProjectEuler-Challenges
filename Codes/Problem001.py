import time
start = time.time()

total = 0
for num in range(3,1000):
    if num % 3 == 0 or num % 5 == 0:
        #sum of the divisible numbers in 3 or 5 with variable total
        total += num
print("Total :",total)

end = time.time()
print("it took {} seconds".format(end - start))
