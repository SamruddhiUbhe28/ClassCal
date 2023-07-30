from add import *
from sub import *

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))

result =0

choice=int(input('''Enter your choice:
	1.Add
	2.Subtract'''))
if choice==1:
	result=addition(num1,num2)
	print("Result is:",result)
elif choice==2:
	result=subtraction(num1,num2)
	print("Result is:",result)
