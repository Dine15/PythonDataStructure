fhand=open("Holi.txt")
print(fhand)

x=fhand.read()
#print(x)

print("Length of the file is:",len(x))
#print("\n")
print(x[:4]) 
#print("\n")
#print("=============")
#print("\n")
z=0
for y in x:
    z=z+1
    print(z,y)
print("Number of lines:", z)