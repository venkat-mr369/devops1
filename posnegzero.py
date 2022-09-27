#Program accepting a numerical Integer value and decides +ve or -ve or zero by using simple if statement
#PosNegZero.py
n=int(input("Enter a Number:")) # n= 0
if(n>0):
	print("{} is +VE".format(n))
if(n<0):
	print("{} is -VE".format(n))
if(n==0):
	print("{} is ZERO".format(n))
print("\nProgram Execution Completed:")