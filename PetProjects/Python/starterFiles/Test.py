#### Class Structure ####
# class person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname,self.lastname)

# y = person("John","Doe") 

# y.printname()

# class Student(person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcome", self.firstname,self.lastname,"to the class of", self.graduationyear)

# x = Student("Antonio","Winn",2020)

# x.welcome()

#### Optimization ####
# from scipy import optimize
# import numpy as np
# import matplotlib.pyplot as plt
# from sympy import *

# d = 28
# a1 = 4.9
# a2 = 3.6
# feedOne = float(input('Feed one mol frac'))
# feedTwo = float(input('Feed two mol frac'))
# flowRate = float(input('Feed flow rate'))
# disOne = .9
# disTwo = .07


# def Roots(x):
#     return (a1*flowRate * feedOne)/(a1 - x) + (a2*flowRate * feedTwo)/(a2 - x)


# Phi = optimize.root(Roots, 4)
# print('The Phi Value is:', Phi.x)

# minimmumVelocity = (a1*d * disOne)/(a1 - Phi.x) + (a2*d * disTwo)/(a2 - Phi.x)
# print('The Minimmum Velocity is:', minimmumVelocity, 'Moles per Second')
# Python code showing use of iter() using OOPs 

#### if Statements ####
# class Counter: 
# 	def __init__(self, start, end): 
# 		self.num = start 
# 		self.end = end 

# 	def __iter__(self): 
# 		return self

# 	def __next__(self): 
# 		if self.num > self.end: 
# 			raise StopIteration 
# 		else: 
# 			self.num += 1
# 			return self.num - 1
			
			
# Driver code 
# if __name__ == '__main__' : 
	
# 	a, b = 1, 5
	
# 	c1 = Counter(a, b) 
# 	c2 = Counter(a, b) 
	
# 	# Way 1-to print the range without iter() 
# 	print ("\nPrint the range without iter()\n") 
	
# 	for l in c1: 
# 		print ("Eating more Pizzas, couting ", l)#,end ="\n") the end="\n" is built in to create new lines however placing " "...
# 		#...shall make all one line
	
# 	print ("\nPrint the range using iter()\n") 
	
# 	# Way 2- using iter() 
# 	obj = iter(c2) 
# 	try: 
# 		while True: # Print till error raised 
# 			print ("Eating more Pizzas, couting ", next(obj)) 
# 	except: 
# 		# when StopIteration raised, Print custom message 
# 		print ("\nDead on overfood, GAME OVER") 

### Calling Libraries ###
# import pathlib
# p = pathlib.Path('.')
# [x.stem for x in p.glob('*.py')]

### DataFrame Example ###
def Example(x):
    print(x +"L")
    return x + "L"

import pandas as pd
import numpy as np

x = [{'user':"A",'filler':"B"},{'user':"B",'filler':"B"},{'user':"C",'filler':"B"},{'user':"D",'filler':"B"}]
user_data = {}
fields = ["user","filler"]

for field in fields:
  user_data[field] = []
  for d in x:
    user_data[field].append(d[field])

# df = pd.DataFrame.from_dict(user_data,orient='index')
df = pd.DataFrame.from_dict(user_data)
# print(df)
# print(df.loc[3].at['user'])
# print(df.apply(Example,axis = 0))
# print(df.apply(np.sum,axis = 1))
# z = df.apply(Example,axis = 1)
# print(z.loc[0].at['filler'])
