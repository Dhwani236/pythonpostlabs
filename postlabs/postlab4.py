from collections import Counter
#1
list1,product=(2,15,90,23,45,67,80),1

for i in list1:
        product=product*i
print(product)
# except ValueError:
#     print("only numeric values will be accepted:")
#use try except while accepting values from user

#2
list2=(1000,876,45,32,1,5,90,10000)
maxvalue=max(list2)
print(f"the largest number in the given list is:{maxvalue}")

#3
list3=(2,2,4,8,9,10,15,18,19,18,15)
uniquelist=list(set(list3))
print(f"new list with eliminated duplicate elements is: {uniquelist}")

#4
list4=(2,2,4,8,9,10,15,18,2,19,18,15,4,5,5,8,8)
frequency=Counter(list4)
print(frequency)
#count is for checking the occurence of the element we are passing as the arguement whereas frequency of elements means checking 
#the number of times each element is occuring
#for example: if i want to check the occurence of 2 in a given list, id use: check2=list4.count(2)
#whereas if a list has (1,1,1,2,4,5,5,8,3,8,2,1) and i want to check the occurence of 1,2,3,4,5,8: i will use the counter function from the collections module 

#5
list5=(1,2,3,4,5)
list6=(5,6,7,8,9,4)
common=set(list5).intersection(set(list6)) #converting both lists to sets because a set only stores original/non-repeating/unique values from a list
#hence intersection finds elements after both lists are filtered into sets - containing only unqiue values
#converting the set with common elements back to a list
common=list(common)
print(f"The common elements from both lists are: {common}")

#6
list7,x=(1,2,3,4,5),''
for i in list7:
        x=x+str(i) #converting each element in the list to string and concatenating those individual strings together
x=int(x) #until this line x was '12345' i.e a string. now x gets converted to integer which means this entire block i.e 12345 gets converted to integer not just integer
print(f"Multiple integers of the list into single integer:{x}")

