import time
start = time.time()

def len_chain(num):
    number = num
    result = 1
    while number > 1:
        if number in cache:
            result += cache[number] - 1
            break
        elif number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        result += 1
    
    if num not in cache:
        cache[num] = result
    return result


cache = {}
longest_chain = 0
starting_num = 0
for i in range(13, 999999):
    chain = len_chain(i)
    if chain > longest_chain:
        longest_chain = chain
        starting_num = i

print("the longest chain contain",longest_chain,"sectors and the starting number is:",starting_num)
        
end = time.time()
print("it took {} seconds".format(end - start))
