data ="From dinesh.tripathi@infosys.com Wed 26 09:18:56 2020"
a=data.find("@")
print("index of @:",a) 
b=data.find(" ",a) 
##It will find the index number of the character and we can 
#specify the index number after which the character should be present.

print(b)

c=data[a+1:b]
print(c)  ## getting the email id from the whole info using slicing

