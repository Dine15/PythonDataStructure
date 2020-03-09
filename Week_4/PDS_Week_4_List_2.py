abc="With Three Words"
a=abc.split()  
##Split method will convert the string into a list where a space will decide the element.
print(a)
print(len(a))
print("\n")


c="We;are;not;going;there"
d=c.split(';')  ##We can have aown customised dlimiter by defining it in the apostrophe in the parenthesis in split method as argument.
print(d)
