num1=int(input("Enter number1:\n"))
num2=int(input("Enter number2:\n"))
operation=int(input("Enter the Operation which is to be performed +,-,*,/,//,**\nType 1 for + Addition\nType 2 for - Subtraction\nType 3 for * Multiplication\nType 4 for Division\nType 5 for // Floor Division\nType 6 for ** Exponential operation\nType 7 for Modulus operation\n"))
if(operation==1):
    print(f"sum of {num1} and {num2} is: {num1+num2}")
elif(operation==2):
    print(f"Difference between {num1} and {num2} is: {num1-num2}")
elif(operation==3):
    print(f"Product of {num1} and {num2} is: {num1*num2}")
elif(operation==4):
    print(f"Division of {num1} by {num2} is: {num1/num2}")
elif(operation==5):
    print(f"Floor Division of {num1} and {num2} is: {num1//num2}")
elif(operation==6):
    print(f" {num1} raised to the power of {num2} is: {num1**num2}")
elif(operation==7):
    print(f"Modulus of {num1} and {num2} is: {num1%num2}")