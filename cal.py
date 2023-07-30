from add import *
from sub import *
from mult import *

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))

result =0

choice=int(input('''Enter your choice:
	1.Add
	2.Subtract
	3.multiplication'''))
if choice==1:
	result=addition(num1,num2)
	print("Result is:",result)
elif choice==2:
	result=subtraction(num1,num2)
	print("Result is:",result)
elif choice==3:
	result=multiplication(num1,num2)
	print('result is',result)
