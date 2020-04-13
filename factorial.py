#!/usr/bin/python3

#RECURSION EXAMPLE
#factorial function
def factorial(vNum):
	if vNum==1:
		return 1
	else:
		return vNum*factorial(vNum-1)
	
print("\t\t\t FACTORIAL ")
num=int(input("Enter number: "))

print("The factorial of",num,"is: ",factorial(num),"\n")
