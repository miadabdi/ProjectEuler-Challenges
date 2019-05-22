from time import time
start = time()

f1 = 1
f2 = 1
counter_round = 1
while True:
    if len(str(f1)) == 1000:
        print("the index of the first term in the Fibonacci sequence is:",counter_round)
        break
    counter_round += 1
    f1 , f2 = f2 , f1 + f2
print("it took {} seconds".format(time() - start))
