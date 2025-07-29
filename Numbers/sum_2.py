#Sum of 2 numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
    sum = int(num1) + int(num2)
except:
    print("Error: letter was entered")
else:
    print("Sum = ",sum)