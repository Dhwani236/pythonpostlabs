import csv
# 1
line_count=0
word_count=0
character_count=0
with open("C:/Users/dhwan/OneDrive/Documents/college/SEM3/pwp/test.txt") as file1:
    for line in file1:
        if line.strip():
         line_count=line_count+1
        character_count=character_count+len(line)
        words=line.split()
        word_count=word_count+len(words)
print(f"The line count of file is: {line_count}")
print(f"The character count of file is: {character_count}")
print(f"The word count of file is: {word_count}")

# 2
list1=[]
with open("C:/Users/dhwan/OneDrive/Documents/college/SEM3/pwp/test.txt") as file2:
   for line1 in file2:
      list1.append(line1)
print(list1)
      
# 3
with open ("C:/Users/dhwan/OneDrive/Documents/college/SEM3/pwp/data-1.csv") as file3:
   reader=csv.reader(file3)
   for row in reader:
      print(row)

# 4
with open("C:/Users/dhwan/OneDrive/Documents/college/SEM3/pwp/merged_file.txt",'w') as file4:
   with open("C:/Users/dhwan/OneDrive/Documents/college/SEM3/pwp/test.txt",'r') as file5:
    content1=file5.read()
    file4.write(content1)
    file4.write("\n")
   with open("C:/Users/dhwan/OneDrive/Documents/college/SEM3/pwp/ict.txt",'r') as file6:
    content2=file6.read()
    file4.write(content2)
print(f"The merged text file is: {file4}")