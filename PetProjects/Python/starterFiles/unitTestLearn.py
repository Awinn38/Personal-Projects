
# Python code to demonstrate the use of 'sys' module
# for command line arguments
 
import sys
 
# command line arguments are stored in the form
# of list in sys.argv
argumentList = sys.argv
print (argumentList)
 
# Print the name of file
print (sys.argv[0])
print(type(sys.argv[1]))