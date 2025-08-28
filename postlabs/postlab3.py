#1
string1='Hello my name is Dhwani'
newstring=string1[::-1]
print(newstring)

#2
string2=input("Enter your string:")
newstring2=string2[::-1]
if(newstring2==string2):
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")

#3
string3=input('Enter your string:')
if(string3.isdigit()):
    print("The given string contains only digits")
else:
    print("The given string does not contain digits")


#4
string4=input('Enter your string:')
words=string4.split()
temp=""
for word in words:
    if(len(word)>len(temp)):
        temp=word
print(f"longest word in the entered string is:{temp}")