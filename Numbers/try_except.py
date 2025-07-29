#Show error when number is greater than 10
num = int(input("Enter a number: "))
try:
    if(num>100):
        raise("Greater than 100")
except:
    print("Not valid")
else:
    print("Valid")