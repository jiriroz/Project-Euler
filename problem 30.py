import time

def Main():
	start_time = time.time()
	total = 0
	powers = []
	for x in range(10):
		powers.append(x**5)
	for x in range(2,999999):
		sum = 0
		for y in str(x):
			sum += powers[int(y)]
		if sum == x:
			total += x
	print (total)
	print (str(time.time()-start_time)+' seconds')

if __name__ == '__main__':
	try:
		Main()
	except Exception as e:
		print (e)

input()