list=[]

while True:  #This comment is very imp and it will help to make a loop which will go on till we want.
    ##Always remember this-> Very imp
    x= input("Enter a number:")
    if x == "Done":
        break 
    list.append(float(x))
    
print("The average of the number in the list is:",((sum(list))/(len(list))))
    

