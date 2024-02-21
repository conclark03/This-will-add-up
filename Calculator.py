# Define Functions
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,Y):
    return x*Y
def divide(x,y):
    if y==0:
        return "Error: Division by Zero!"
    else:
        return x/y
# Display Operations
    print ("Select Operation:")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
# User Input
Choice = input("Enter Choice (1,2,3,4):")
num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))
#Perform Operation Based on User Choice
if Choice=='1':
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif Choice=='2':
    print(f"{num1} - {num2} = {subtract(num1,num2)}")
elif Choice=='3':
    print(f"{num1} * {num2} = {multiply(num1,num2)}")
elif Choice == '4':
    result = divide(num1, num2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"{num1} / {num2}")
else: print ("Invalid Input")
