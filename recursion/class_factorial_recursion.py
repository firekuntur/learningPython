#!/usr/bin/python3

#              CLASSES AND RECURSION EXAMPLE

#class initiation
class factorialClass:
	#variables
	vNum=0
	vResult=0

	def __init__(self):
		#clear vars for next obj--just in case
		vNum=0
		vResult=0

	#calculate factorial function in recursive fashion
	# x var is temp var sent to the obj	
	def calcFactorial(self,x):
		if x==1:
			return x
		else:
			self.vResult = x * self.calcFactorial(x-1)
			return self.vResult
	#returns results
	def getResult(self):
		return self.vResult
def main():	
	print("\t\t\t FACTORIAL ")
	num=int(input("Enter number: "))
	fct=factorialClass()
	fct.calcFactorial(num)
	print("The factorial of",num,"is: ",fct.getResult(),"\n")

#program loads
if __name__=="__main__":
	main()
