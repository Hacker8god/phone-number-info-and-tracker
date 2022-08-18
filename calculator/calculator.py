from importlib.resources import Package
from inspect import Parameter
from turtle import circle
from pip import main
from json import tool
from symtable import Symbol
print("hlo user...")
print("1. Calculator")
print("2. Even odd checker")
print("3. Factorial printer")
print("4. Tabel printer")
print("5. Circle functions")
print("6. Reactangle functions")
tool_m=int(input("choose your tool..( 1-5): "))
if tool_m==1 :
    print(" Calculator")
    print("+. Add")
    print("-. Subtract")
    print("x. Multiply")
    print("/. Divide")  
    print("%. Modulus")

    task=input(("Enter choice (+ , - , x , / , % )"))
    if task=='+':
        a=float(input("Enter A:"))
        b=float(input("Enter B:"))

        c=a+b
        print("Sum = ", c )
    elif task=='-':
        a=float(input("Enter A:"))
        b=float(input("Enter B:"))
        c=a-b 
        print("Substract = ", c )
    elif task=='x':
        a=float(input("Enter A:"))
        b=float(input("Enter B:"))
        c=a*b
        print("Product = ", c )
    elif task=='/':
        a=float(input("Enter A:"))
        b=float(input("Enter B:"))  
        c=a/b
        print( a ,"/", b ,"=", c )
    elif task=='%':
        a=float(input("Enter A:"))
        b=float(input("Enter B:"))
        c=a%b
        print( a ,"%", b ,"=", c )
    else:
        print("invalid choice")
elif tool_m==2:
    print("Even odd checker")
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))
elif tool_m==3 :
    print("Factorial printer")
    fact = 1
    n=int(input("enter the number "))
    for i in range(1,n+1):
            fact = fact * i      
    print ("The factorial of",n , "is : ",fact )
elif tool_m==4:
    print("Tabel printer")
    i=1
    n=int(input("Enter a number : "))   
    while i<=10:
        print(n,"x",i,"=",i*n)
        i+=1
elif tool_m==5:
    print("Circle functions..")
    print("1. Area of circle")   
    print("2. Circumference of circle")
    task=int(input("Enter task 1,2 : "))
    if task==1:
        radius=float(input("Enter thr Radius : "))
        area=3.14*radius*radius
        print("Area of circle is : ",area)
    elif task==2:
        radius=float(input("Enter thr Radius : "))
        Circumference=2*3.14*radius
        print("Circumference of circle id :",Circumference)
    else :
        print("Invalid selection")
elif tool_m==6:
    print("Reactangle functions")
    print("1. Area of reactangle")
    print("2. Parameter of reactangle")
    task=int(input("Enter the task 1,2 : "))
    if task==1:
        hight=float(input("Enter thr Length: "))
        width=float(input("Enter thr Breadth : "))
        area=hight*width
        print("Area of Reactangl is : ",area )
    elif task==2:
        hight=float(input("Enter thr Length: "))
        width=float(input("Enter thr Breadth : "))
        parameter=2*(hight+width)
        print("Parameter of Reactangle is :" ,parameter)
    else :
        print("Invalid selection")
        






else:
    print("invalid selection")

