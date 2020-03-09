d={'x':99,'a':21,'A':34}
print(d)
tmp=[]
for k,v in d.items():
    tmp.append((v,k))
print(tmp) 
tmp=sorted(tmp)
print(tmp)
tmp=sorted(tmp,reverse=True)
print(tmp)