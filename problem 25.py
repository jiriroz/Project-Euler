import time

def Main():
	start_time = time.time()
	fib = [1,1]
	x = 1
	while len(str(fib[-1]))<1000:
		fib.append(fib[x-1] + fib[x])
		x +=1
	print (x)
	print (str(time.time()-start_time)+' seconds')
	

if __name__ == '__main__':
	try:
		Main()
	except Exception as e:
		print (e)

input()