class Person:
    def print_name(self,name):
        print("My name is: "+name)
    def add(self,a,b):
        print("Sum = ",a+b)
    def sub(self,a,b):
        print("Difference = ",a-b)

person = Person()
person.print_name("Ajith")
person.add(2,3)
person.sub(8,3)