import time
start = time.time()

def factorial(num):
    result = 1
    for i in range(num,1,-1):
        result *= i
    return result

def count_paths_grid(col,row):
    # Paths equels to factorial of columns + rows divided into factorial of columns * factorial of rows
    return int(factorial(col + row) / (factorial(col) * factorial(row)))
    
print("the paths is:",count_paths_grid(20, 20))

end = time.time()
print("it took {} seconds".format(end - start))
