#a
#occurences of a single element in a tuple so count method/function
#count works for strings, lists and tuples
tuple1=(1,10,6,3,1,4,8,1,3,10,3,10,4,8,5,8,10,2,4,10)
check=tuple1.count(10)
print(f"occurence of 10 in the given tuple is: {check}")


#b
print(9 in tuple1) #returns true if element is present and false otherwise 
# we can also use the index method where it returns the index of the element we want to check the presence of, in case it's present and generates ValueError otherwise
# actually index method only checks the first occurence of the element we are passing as an arguement and returns the index where it's first spotted
# for example: tuple=(1,3,2,1,4) now number 1 is at indices 0 and 3. so index method will return the index where 1 is spotted first, here at 0
# but this method can be used as an alternative for "in" too
# in case we do not want to show ValueError we can use try and except
#try:
  #print(tuple1.index(9))
#except ValueError:
  #print("the element is not present in the tuple")

#c
tuple2,x=('hello',1,2,3,10.28,'Dhwani'),'' #tuples are heterogeneous
for i in tuple2:
    x=x+str(i) #converting each element of the tuple into string and then concatenating those elements to form a single string x
print(f"the tuple converted to string is:{x}")


#d
tuple3=(999,10000,9876452,1,5,90,89,1456728,100)
max_element=max(tuple3)
min_element=min(tuple3)
print(f"the maximum and minimun elements from the given tuples are:{max_element} and {min_element}")


#e
tuple4,x=('hi','diya','dhwani','sarcasm','always','fighting'),''
# since these elements are already strings we do not need to conver them to strings
# just iterate a loop to concatenate them together
for i in tuple4:
    x=x+i
print(f"the concatenated string is: {x}")


#f
tuple5=(45,1,36,98,100,23,1000,22,19,14)
sortedtuple=sorted(tuple5)
print(f"given tuple sorted in ascending order is: {sortedtuple}")
#for descending order: sortedtuple=sorted(tuple5,reverse=True)

#g
tuple5=(45,1,36,98,100,23,1000,22,19,14)
#first element can be found using index 0
first=tuple5[0]
# for last element: first find the length of the tuple because we do not know that
# and then length-1 ka index position pe last element will be there
last=tuple5[len(tuple5)-1]
print(f"first element of the given tuple is: {first} and last element is {last}")
