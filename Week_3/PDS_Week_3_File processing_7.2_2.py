fname=input("Enter the file name:")
try:
    fhand=open(fname)
except:
    print("Bad file name")
    print("File cannot be opened: ",fname)
    quit()

count=0
for line in fhand:
    if line.startswith("Holi"):
        print(line.rstrip())
        count=count+1
print("There are around",count, "lines in the file.")




   