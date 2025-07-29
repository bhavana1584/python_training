class Person:
    def printName(self,name):
        print(name)

class Ashok(Person):
    def printDetails(self):
        print("Something")

obj = Ashok()
obj.printName("Alexander")