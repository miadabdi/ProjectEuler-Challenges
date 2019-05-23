from time import time
start = time()

def ReciprocalCycles(d):
    values = []
    num = 1
    while (num % d) not in values:
        if num % d:
            values.append(num % d)
        else:
            break
        num = int(str(num % d) + '0')
    return values

longest = 0
for i in range(2, 1000):
    if longest < len(ReciprocalCycles(i)):
        longest = len(ReciprocalCycles(i))
        d = i
print("The longest recurring cycle belongs to: ", d)
print("it took {} seconds".format(time() - start))
