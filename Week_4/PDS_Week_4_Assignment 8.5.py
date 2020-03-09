##mbox-short.txt

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
list=[]
count=0
fhand=open(fname)
for i in fhand:   ##This is very imp to remember 
    if i.startswith("From")==True and i.startswith("From:")==False:
        count=count+1
        l=i.split()
        list.append(l[1])
for i in list:
    print(i)

print("There were", count, "lines in the file with From as the first word")

 
#print(fhand.read())
#fread=fhand.read()
#list=fread.split()
#for i in list:
#    if i.endswith()