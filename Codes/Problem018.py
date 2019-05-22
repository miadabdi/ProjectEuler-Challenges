from time import time
from os import chdir, path
from sys import argv
start = time()

# changing current working directory to the directory of executed file
chdir(path.abspath(path.dirname(argv[0]))) 

# You need Problem018-triangle.txt file in the same directory
file = open('Problem018-triangle.txt')

data = [line.replace("\n", "").replace(" ", ",").split(",") for line in file.readlines()] # this line converts the file into a list of lists
    
data = [[int(elements) for elements in first_list] for first_list in data]     # returns int version of a list strings
data.reverse()

for row_counter, row in enumerate(data):
    if len(row) == 1:
        break
    for index, item in enumerate(row):
        if index+1 == len(row):
            break
        data[row_counter+1][index] += max(item,row[index+1])
file.close()
print("the maximum sum of a path from top to bottom is:",data[-1][-1])

print("it took {} seconds".format(time() - start))
