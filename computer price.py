class Computer:
   
   def __init__(self):
       self.__maxprice = 900
       
   def printPrice(self):
       print(f"Selling Price: {self.__maxprice}")
       
   def setMaxPrice(self, price):
       self.__maxprice = price
       
c1 = Computer()
c1.printPrice()

c1.__maxprice = 1500
c1.printPrice()

c1.setMaxPrice(15000)
c1.printPrice()       
    