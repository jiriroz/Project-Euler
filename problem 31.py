import time

count = 0
values = [1,2,5,10,20,50,100,200]

def counter(val):
	if val == 0:
		global count
		count += 1
	if val <= 0:
		return
	for x in values:
		newval = val - x
		counter(newval)

def Main():
	times = []
	for x in range(30):
		start_time = time.time()
		counter(x)
		times.append((x,time.time()-start_time))
	print (times)
if __name__ == '__main__':
	try:
		Main()
	except Exception as e:
		print (e)

input()