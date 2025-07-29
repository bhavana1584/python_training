# print("Enter range: ")
# num=input()
# i=1
# for i in range (int(num)):
#     print(i+1)


# print("Enter number: ")
# num=int(input())
# if (num%2==0):
#     print("Even")
# else:
#     print("Odd")

# cars = ["a","b","c","d","e"]
# print(len(cars))
# print(cars[0])
# for i in cars:
#     print(i)

list = ["one","two","three","four"]
print(list[0])
try:
    print(list[5])
except Exception as e:
    print("Error in the array")
print("This is the last line")