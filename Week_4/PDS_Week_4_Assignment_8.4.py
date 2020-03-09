fname = input("Enter file name: ")
fhand=open(fname)
fread=fhand.read()
x=fread.split()
list=[]
for i in x:
    if i not in list:
        list.append(i)
list.sort()
print(list)

