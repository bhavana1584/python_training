#Using placeholders in a function
def print_info(name,city):
    print(f"Name is {name}, and city is {city}")

name = input("Enter name: ")
city = input("Enter city: ")
print_info(name, city)