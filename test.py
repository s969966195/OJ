import os

for a, b, c in os.walk(os.getcwd() + '/leetcode'):
    print a
    print b
    print c
    exit()
