import math as m
from math import *
# #a
# degree=float(input('Enter the angle in degree:'))
# radian=degree*(3.14/180)
# print(f"the angle converted to radian is: {radian}")

# #b
# x=int(input("Enter the value for x:"))
# y=6*(x*x)+ 4*(m.sin(x))
# print(y)

#c
#𝑓(𝑥) = 𝑐𝑜𝑠(2𝑥),𝑓′(𝑥) = ―2sin(2𝑥), 𝑎𝑛𝑑 𝑓′′(𝑥) = ―4cos(2𝑥)
def one(x):
    fx=cos(2*x)
    return fx
def two(x):
    fx2=-2*sin(2*x)
    return fx2
def three(x):
    fx3=-4*cos(2*x)
    return fx3
print(one(90))
print