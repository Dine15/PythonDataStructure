##Sorting the dictionary with value order instead of the key order..

c={10:"a",34:"A",43:"r",44:"R"}
print(c.items())

s1=sorted(c.items()) ##sorting by the value order which is kept in key place
s2=sorted(c) ## Only the values which are in key place will get sorted..
print(s1)
print(s2)

lv=[]
lk=[]
for i in s1:
    lv.append(s1[i][0])
    lk.append(s1[i][1])


for i in lv:
    
#list1=[]
#list2=[]
#
#for v,k in s1.items():
#    list1.append(v)
#    list2.append(k)
#    
#sd=dict()
#for i in list2:
#    sd[i]=v
#print(sd)

    
    