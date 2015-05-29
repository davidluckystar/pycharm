import sys

def Hello(name):
	if name == 'Alex':
		print 'Hello Alex =)'
	else:
		name = name + '!!!'
		print 'Hello', name

def Factorial(fac):
	if fac > 1:
		return fac * Factorial(fac-1)
	
def KeyFunction(val):
	return len(val)
	
def SortFunction(list):
	return sorted(list, key=KeyFunction)
	
def Loop():
	for el in [1,2,3]:
		print el
	
def main():
	Hello(sys.argv[1])
	a = SortFunction(['sdf','ag','gawgwgwg','d','gaweg','wegweg'])
	print(a)
	#Factorial(5)
	
if __name__ == '__main__':
	main()