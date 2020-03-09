name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand=open(name)
l=[]
for i in fhand:
    i.rstrip()  ## By Sir code so I modified it respectively
    if i.startswith("From"):
        l.append(i)
        
#print(l)
k1=[]
k2=[]
for i in l:
    if i.startswith("From") ==True and i.startswith("From:")==False:
        x=i.split()
        k1.append(x[1])
    elif i.startswith("From:"):
        x=i.split(":")
        k2.append(x[1])
#print(k1,len(k1))
#print(k2,len(k2))

k=k1+k2
d=dict()
for i in k:
    d[i] = d.get(i,0)+1  ##Construction of dictionary
    
#print(d.items())

emailid=None
count=0
for k,v in d.items():
    if count == 0 or count<v:
        emailid=k
        count=v
        
print(emailid,count)

