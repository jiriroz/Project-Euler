file = open('problem 18.txt','r')
triangle = file.read()
file.close()
triangle = triangle.split('\n')
numbers = []
for x in triangle:
	x = x.split(' ')
	numbers.append(x)

def add_one(num):
	num = list(num)
	for x in range(len(num)-1,-1,-1):
		if num[x] == '0':
			num[x] = '1'
			break
		num[x] = '0'
	return ''.join(num)

def compute_sum(numbers):
	highest = 0
	path = '0'*(len(numbers)-1)
	while True:
		sum = int(numbers[0][0])
		index = 0
		for x in range(1,len(numbers)):
			index += int(path[x-1])
			sum += int(numbers[x][index])
		if sum > highest:
			highest = sum
		if '0' not in path:
			return highest
		path = add_one(path)
	return highest

print (compute_sum(numbers))

input()