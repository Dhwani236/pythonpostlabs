class Circle:
    def __init__(self,radius):
     self.radius=radius

    def areaofcircle(self):
        return f"area: {3.14*self.radius*self.radius}"
    
    def perimeterofcircle(self):
       return f"perimeter: {2*3.14*self.radius}"
    
circle1=Circle(10)
print(circle1.areaofcircle())
print(circle1.perimeterofcircle())

# Circle is the class, circle1 is the object and radius is the attribute of the object circle1


class Books:
   def __init__(self,title,author,price):
    self.title=title
    self.author=author
    self.price=price
  
   def bookdetails(self):
      return f"BookTitle: {self.title}, BookAuthor: {self.author}, BookPrice:{self.price}, DiscountOf: {0.1*self.price}"
   def updatedprice(self):
      return f"Updated Price: {self.price-0.1*self.price}"
   
testbook1=Books("Perks of Being A Wallflower", "Stephen Chbosky", 250)
print(testbook1.bookdetails())

testbook2=Books("The Fault in Our Stars","John Green",150)
print(testbook2.bookdetails())
print(testbook2.updatedprice())


   
   

   
