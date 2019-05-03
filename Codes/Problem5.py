import time
start = time.time()

def divisible_by_1to20(num):
    #if the argument is dividiable by 1 to 20 returns "True"
    for i in range(11,21):
        # if a number is divisibale by 11 to 20, it means it is divisibale by 1 to 10 as well
        if num % i != 0:
           return False
    return True 

for i in range(2520,10000000000,2520):
    if divisible_by_1to20(i):
        print("The first divisible number by 1 to 20:",i)
        break

end = time.time()
print("it took {} seconds".format(end - start))
