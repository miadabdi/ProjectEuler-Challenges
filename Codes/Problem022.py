import os, time, sys
from sys import argv
from os import chdir, path
start = time.time()

# changing current working directory to the directory of executed file
chdir(path.abspath(path.dirname(argv[0])))

# Problem022-names.txt file should be in the same directory as this file is
names = open("Problem022-names.txt", 'r')

def get_score_name(name):
    return sum([ord(letter) - 64 for letter in name])

names = sorted([item.replace('"', '') for item in names.read().split(",")]) # converting the text file to a usable list
sum_all_score_names = sum([get_score_name(name) * (index + 1) for index, name in enumerate(names)])

print("sum of all score of names:",sum_all_score_names)
print("it took {} seconds".format(time.time() - start))
