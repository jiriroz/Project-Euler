import time
import math

MARGIN = 28124

def findAbundant(margin):
	abundants = []
	for x in range(1,margin):
		sum = 1
		for y in range(2,int(math.sqrt(x))+1):
			if x % y == 0:
				sum += y
				if (x/y != y):
					sum += x/y
		if sum > x:
			abundants.append(x)
	return abundants

def findSums(lst):
	sums = []
	for x in range(len(lst)):
		for y in range(x,len(lst)):
			if lst[x]+lst[y] < MARGIN:
				sums.append(lst[x]+lst[y])
	return sums

def findNonAbundantSums(lst):
	sums = []
	bitmap = [0] * MARGIN
	for x in lst:
		bitmap[x] = 1
	for i in range(MARGIN):
		if bitmap[i] == 0:
			sums.append(i)
	return sums

def Main():
	start_time = time.time()
	abundants = findAbundant(MARGIN)
	sums = findSums(abundants)
	result = findNonAbundantSums(sums)
	print (sum(result))
	print (str(time.time()-start_time)+' seconds')

if __name__ == '__main__':
	try:
		Main()
	except Exception as e:
		print (e)

input()