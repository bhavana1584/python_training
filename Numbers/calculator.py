# Simple calculator
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

try:
    us = input("Enter function: ")
    n1 = input("Enter number 1: ")
    n2 = input("Enter number 2: ")

    if(us.isnumeric()==False):
        raise Exception("Invalid function input")
    if(n1.isnumeric()==False):
        raise Exception("number 1 is a string")
    if(us.isnumeric()==False):
        raise Exception("number 2 is a string")

    user = int(us)
    num1 = int(n1)
    num2 = int(n2)

    match user:
        case 1:
            print("Sum = ",num1+num2)
        case 2:
            print("Difference = ",num1-num2)
        case 3:
            print("Product = ",num1*num2)
        case 4:
            print("Quotient = ",num1/num2)
        case _:
            print("Invalid function input")
except Exception as e:
    print(e)