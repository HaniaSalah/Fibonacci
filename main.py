loop= int(input("Enter number of loops: "))
count=1
n1 = 0
n2= 1
nextNumber = n2

while count<=loop:
    print ("Current number is: ",n1)
    count +=1
    n1 = n2
    n2 = nextNumber
    nextNumber = n1 + n2
