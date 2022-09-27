#Program for implementing all types of Arithmetic Operations with menu driven application with match case concept.
#aopmenuappl.py
import sys
print("="*50)
print("\tArithmetic Operations")
print("="*50)
print("\t1.Addition")
print("\t2.Substraction:")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("="*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
	
	case 1:
			a,b=float(input("Enter Value of a :")),float(input("Enter Value of b :"))
			print("\tsum({},{})={}".format(a,b,a+b))
	case 2:
			a,b=float(input("Enter Value of a :")),float(input("Enter Value of b :"))
			print("\tsub({},{})={}".format(a,b,a-b))
	case 3:
			a,b=float(input("Enter Value of a :")),float(input("Enter Value of b :"))
			print("\tmul({},{})={}".format(a,b,a*b))
	case 4:
			a,b=float(input("Enter Value of a :")),float(input("Enter Value of b :"))
			print("\tdiv({},{})={}".format(a,b,a/b))
			print("\tFloor Div({},{})={}".format(a,b,a//b))
	case 5:
			a,b=float(input("Enter Value of a :")),float(input("Enter Value of b :"))
			print("\tmod({},{})={}".format(a,b,a%b))
	case 6:
			a,b=float(input("Enter Base :")),float(input("Enter Power :"))
			print("\tpow({},{})={}".format(a,b,a**b))
	case 7:
			print("Thx for using this program!")
			sys.exit()	
	

print("Program execution completed:")	

