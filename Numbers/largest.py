# Largest of three numbers
num1 = input("Enter number1: ")
num2 = input("Enter number2: ")
num3 = input("Enter number3: ")

try:
    if(num1.isnumeric()==False):
        raise Exception("number1 is a string")
    if(num2.isnumeric()==False):
        raise Exception("number2 is a string")
    if(num3.isnumeric()==False):
        raise Exception("number3 is a string")
    large = int(num1)
    if(int(num2)>large):
        large = int(num2)
    if(int(num3)>large):
        large = int(num3)
    print("Largest = ",large)
except Exception as e:
    print(e)