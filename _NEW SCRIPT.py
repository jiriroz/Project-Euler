import os
content = \
"import time\n\n"+\
"def Main():\n"+\
"	start_time = time.time()\n\n"+\
"	print (str(time.time()-start_time)+' seconds')\n\n"+\
"if __name__ == '__main__':\n"+\
"	try:\n"+\
"		Main()\n"+\
"	except Exception as e:\n"+\
"		print (e)\n\n"+\
"input()"


name = input("File name: ")
name = name + ".py"
if name != '.py':
	newscript = open(name,'w')
	newscript.write(content)
	newscript.close()