import time

def Main():
	start_time = time.time()

	for x in range(1,20):
		print (1/x, 1000/(x*1000))
		
		
	
	
	
	
	
	
	
	
	print (str(time.time()-start_time)+' seconds')

if __name__ == '__main__':
	try:
		Main()
	except Exception as e:
		print (e)

input()