##PROJECT 1
##DATE CREATED--28th JUNE 2025
##STATUS--READY TO BE PUSHED ON GITHUB

##SIMPLE CALCULATOR IN PYTHON (TO BE PUSHED IN GITHUB AS FIRST PROJECT)
# def add(x,y):
#     return(x+y)
# def subtract(x,y):
#     return(x-y)
# def multiply(x,y):
#     return(x*y)
# def divide(x,y):
#     if y==0:
#         return("Error, cannot divide by zero")
#     return(x/y)
# def power(x,y):
#     return(x**y)
# def square_root(x):
#     return(x**0.5)
# try:
#     num1=float(input("enter number 1"))
#     num2=float(input("enter number 2"))
# except ValueError:
#     print("Invalid entry. Please enter only numbers")
#     exit()

# print("\nChoose an operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Power")
# print("6. Square Root")

# z=int(input("enter a choice"))
# if z==1:
#     print("Sum is",add(num1,num2))
# elif z==2:
#     print("Subtracted value",subtract(num1,num2))
# elif z==3:
#     print("Product",multiply(num1,num2))
# elif z==4:
#     print(num1,"divided by",num2,"is",divide(num1,num2))
# elif z==5:
#     print(num1,"raised to the power of",num2,"is",power(num1,num2))
# elif z==6:
#     num3=float(input("enter the number"))
#     if num3<0:
#         print("Cannot find square root of negative number")
#     else:
#         print("Square Root of",num3,"is",square_root(num3))
# else:
#     print("Invalid Input. Please enter a correct choice.")