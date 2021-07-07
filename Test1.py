# Python code showing use of iter() using OOPs 

class Counter: 
	def __init__(self, start, end): 
		self.num = start 
		self.end = end 

	def __iter__(self): 
		return self

	def __next__(self): 
		if self.num > self.end: 
			raise StopIteration 
		else: 
			self.num += 1
			return self.num - 1
			
			
# Driver code 
if __name__ == '__main__' : 
	
	a, b = 1, 5
	
	c1 = Counter(a, b) 
	c2 = Counter(a, b) 
	
	# Way 1-to print the range without iter() 
	print ("\nPrint the range without iter()\n") 
	
	for l in c1: 
		print ("Eating more Pizzas, couting ", l)#,end ="\n") the end="\n" is built in to create new lines however placing " "...
		#...shall make all one line
	
	print ("\nPrint the range using iter()\n") 
	
	# Way 2- using iter() 
	obj = iter(c2) 
	try: 
		while True: # Print till error raised 
			print ("Eating more Pizzas, couting ", next(obj)) 
	except: 
		# when StopIteration raised, Print custom message 
		print ("\nDead on overfood, GAME OVER") 
