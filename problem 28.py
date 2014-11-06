import time

def Main():
	start_time = time.time()
	nums = [1]
	dist = 2
	counter = 4
	while dist < 1001:
		nums.append(nums[-1] + dist)
		counter -= 1
		if counter == 0:
			counter = 4
			dist += 2
	print (sum(nums))
	
	print (str(time.time()-start_time)+' seconds')

if __name__ == '__main__':
	try:
		Main()
	except Exception as e:
		print (e)

input()