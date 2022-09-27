#Program for generating 1 to n number where n is +ve
#NumGenEx1.py
n=int(input("Enter Value of n:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	#generate 1 to n
	i=1 # Initlization Part
	while(i<=n):   # Cond Part
		print("\t{}".format(i))
		i=i+1 # Updation Part
