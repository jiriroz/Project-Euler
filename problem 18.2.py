file = open('problem 18.txt','r')
triangle = file.read()
file.close()
triangle = triangle.split('\n')
numbers = []
for x in range(len(triangle)):
	triangle[x] = triangle[x].split(' ')
	for y in range(len(triangle[x])):
		triangle[x][y] = int(triangle[x][y])

def add_line(triangle):
	index = len(triangle)-2
	for y in range(len(triangle[len(triangle)-2])):
		triangle[index][y] += max([triangle[index+1][y],triangle[index+1][y+1]])
	triangle = triangle[:len(triangle)-1]
	if len(triangle) == 1:
		return triangle[0][0]
	return add_line(triangle)

print (add_line(triangle))
input()