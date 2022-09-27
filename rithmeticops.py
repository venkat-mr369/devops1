#Program for implementing all types of Arithmetic Operations with menu driven application with match case concept.
#arithmeticops.py
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
ch=int(input("Enter your Choice:"))
match(ch):
	
	case 1:
			a,b=int(input("Enter Value of a :")),int(input("Enter Value of b :"))
			print("\tsum({},{})={}".format(a,b,a+b))
	case 2:
			a,b=int(input("Enter Value of a :")),int(input("Enter Value of b :"))
			print("\tSubstraction({},{})={}".format(a,b,a-b))
	case 3:
			a,b=int(input("Enter Value of a :")),int(input("Enter Value of b :"))
			print("\tMultiplication({},{})={}".format(a,b,a*b))
	case 4:
			a,b=int(input("Enter Value of a :")),int(input("Enter Value of b :"))
			print("\tDivision({},{})={}".format(a,b,a/b))
			print("\tFloor Div({},{})={}".format(a,b,a//b))
	case 5:
			a,b=int(input("Enter Value of a :")),int(input("Enter Value of b :"))
			print("\tmod({},{})={}".format(a,b,a%b))
	case 6:
			a,b=int(input("Enter Base :")),int(input("Enter Power :"))
			print("\tpower of({},{})={}".format(a,b,a**b))
	case 7:
			print("Thx for using this program!")
			sys.exit()	
	

print("Program execution completed:")	
