#1
length=float(input("Enter the length of the rectangle: "))
breadth=float(input("Enter the breadth of the rectangle:"))
area=float(length*breadth)
print(area)
perimeter=float(2*(length+breadth))
print(perimeter)

#2
number=int(input("Enter your number:"))
if(number%2==0):
    print("the number is even")
else:
 print("the number is odd")

#3
side=float(input("Enter the side of the cube:"))
area=(6*side**2)
print(f"area of cube is {area}")
volume=(side**3)
print(f"volume of cube is {volume}")

#4
x=float(input("Enter the value for x:"))
y=float(input("Enter the value for y:"))
z1=(x+y)*(x-y)
print(f"the value of z is:{z1}")

#5
x=float(input("Enter the value for x:"))
y=float(input("Enter the value for y:"))
z2=(x+y)*(x+y)-2*x*y
print(f"the value of z is:{z2}")

#6
temperature=float(input("Enter the temperature in Celsius:"))
result=(9/5*temperature)+32
print(f"temperature in Farenheit:{result}")