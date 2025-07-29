# Positive, negative, zero
num = input("Enter a number: ")
try:
    if(int(num)>0):
        print("Positive")
    elif(int(num)<0):
        print("Negative")
    else:
        print("Zero")
except:
    print("Error: you entered a string")