import os
path = r'' + os.getcwd()
fo = open('problem 11.txt','r')
n = fo.read()
fo.close()

sequence = 4

n = n.split('\n')
lst = []
for x in n:
    x = x.split(' ')
    lst.append(x)

horizontalList = []
verticalList = []
diagonalList = []

def horizontal(horizontalList,lst,sequence):
    for x in lst:
        for y in range(len(x)):
            multiple = 1
            for z in x[y:y+sequence]:
                multiple = int(z)*multiple
            horizontalList.append(multiple)
    return max(horizontalList)

def vertical(verticalList,lst,sequence):
    for y in range(len(lst)):
        for x in range(len(lst[0])-sequence):
            multiple = 1
            for z in range(sequence):
                multiple = multiple*int(lst[x+z][y])
            verticalList.append(multiple)
    return max(verticalList)

def diagonal(diagonalList,lst,sequence): 
    for y in range(len(lst[0])-sequence):
        for x in range(len(lst)-sequence):
            multiple = 1
            for z in range(sequence):
                multiple = multiple*int(lst[x+z][y+z])
            diagonalList.append(multiple)
        for x in range(sequence,len(lst)):
            multiple = 1
            for z in range(sequence):
                multiple = multiple*int(lst[x-z][y+z])
            diagonalList.append(multiple)
    return max(diagonalList)


print(horizontal(horizontalList,lst,sequence))
print(vertical(verticalList,lst,sequence))
print(diagonal(diagonalList,lst,sequence))




input()