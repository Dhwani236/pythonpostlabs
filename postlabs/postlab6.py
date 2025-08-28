from collections import Counter
#a
for i in range(1,101,2):
    print(i)
# step of 2 ensures only odd numbers are printed 
# but if we are beginning from 0, step of 2 does not give us odd rather gives even

# #b
# n=int(input("Enter the last limit:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(f"sum of all natural number from 1 to {n} is: {sum}")

# #c
# number=int(input("Enter your number:"))
# digits=len(str(number))
# print(f"the number of digits in the entered number is: {digits}")
# # or finding the length of the number and then iterating a loop from 1 to length+1, count++

# #d
# number=int(input("Enter your number:"))
# new=list(str(number))
# first=new[0]
# last=new[len(new)-1]
# print(f"first digit of the number is: {first} and last digit of the number is: {last}")

#e
number=int(input("Enter your number:"))
new=list(str(number))
first=new[0]
last=new[len(new)-1]
# finding the first and last numbers till here. now swapping them
temp=first
first=last
last=temp
print(f"swapped first {first} and last digit of the numbers are: {last}")
