import os, time, sys
from sys import argv
from os import chdir, path
start = time.time()

# changing current working directory to the directory of executed file
chdir(path.abspath(path.dirname(argv[0])))

# Problem022-names.txt file should be in the same directory as this file is
names = open("Problem022-names.txt", 'r')

def get_score_name(name):
    letter_scores = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,\
    'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    return sum([letter_scores[letter] for letter in name])

names = sorted([item.replace('"', '') for item in names.read().split(",")]) # converting the text file to a usable list
sum_all_score_names = sum([get_score_name(name) * (index + 1) for index, name in enumerate(names)])

print("sum of all score of names:",sum_all_score_names)
print("it took {} seconds".format(time.time() - start))
