from sys import argv
from os import path, chdir
from time import time
start = time()

# changing current working directory to the directory of this file
chdir(path.abspath(path.dirname(argv[0])))

# You need Problem067-triangle.txt file in the same directory
file = open('Problem067-triangle.txt')

data = [i.replace("\n",'').replace(" ",',').split(",") for i in file.readlines()] # this line converts the file into a list of lists
    
data = [[int(element) for element in line] for line in data]  # returns int version of a list strings
data.reverse()

for row_counter, row in enumerate(data):
    if len(row) == 1:
        break
    for item_counter, item in enumerate(row):
        if item_counter+1 == len(row):
            break
        data[row_counter+1][item_counter] += max(item,row[item_counter+1])

file.close()
print("the maximum sum of a path from top to bottom is:",data[-1][-1])
print("it took {} seconds".format(time() - start))
