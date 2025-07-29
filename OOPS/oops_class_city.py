class City:
    def addCityDetails(self,name,country):
        self.name = name
        self.country = country
    def printCityDetails(self):
        print("Name: ",self.name)
        print("Country: ",self.country)

c = City()
c.addCityDetails("Bangalore","India")
c.printCityDetails()

c1 = City()
c1.addCityDetails("Frankfurt","Germany")
c1.printCityDetails()