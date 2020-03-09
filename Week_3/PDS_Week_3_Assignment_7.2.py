# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
l=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    count=count+1
    a=line.find(":")
    b=line[a+1:]
    b=b.strip()
    c=float(b)
    l=l+c
average=l/count
print("Average spam confidence:",average)

