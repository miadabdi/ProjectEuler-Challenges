from time import time
start = time()

def fact(num):
    result = 1
    for i in range(num , 1 , -1):
        result *= i
    return result

def index_perm(digits,index):#finds the value of the index in permutation
    lenght = len(digits)
    result = []
    while len(result) < lenght:
        col = index // fact(len(digits)-1)
        index = index % fact(len(digits)-1)
        result.append(digits[col])
        digits.remove(result[-1])
    return result

digits = [0,1,2,3,4,5,6,7,8,9]
#The index must be 999999, beacause the index of the millionth permutation is not 1000000, it is 999999(index begins 0)
index = 999999

print("the", index+1, "th index in permutation is:", end="")
print("".join([str(x) for x in index_perm(digits,index)]))
print("it took {} seconds".format(time() - start))
