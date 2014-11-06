import os
path = r'' + os.getcwd()
fo = open('problem 13.txt','r')
n = fo.read()
fo.close()

n = n.split('\n')

sum = 0

for x in n:
    sum += int(x)

print (str(sum)[0:10])
input()