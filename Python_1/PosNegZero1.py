#Program accepting a numerical Integer value and decides +ve or -ve or zero by using if ..else statement
#PosNegZero.py
n=int(input("Enter a Number:")) #n= 10
if(n==0):
	print("{} is Zero".format(n))
else:
	if(n>0):
		print("{} is +VE".format(n))
	else:
		print("{} is -VE".format(n))

