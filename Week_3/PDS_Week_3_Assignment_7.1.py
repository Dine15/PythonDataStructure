fhand=open("Holi.txt")
#print(fhand)
##x=fhand.read()
##print(x)
#
#print("============")
x=0
for y in fhand:
    x=x+1
#    print(x,y)

    if y.startswith("Holi"):
        print(x,y)
print("Number of lines:", x)

