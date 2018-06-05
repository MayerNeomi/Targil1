#Neomi Mayer 328772801
#1
while True:
    a=int(input("line one:"))
    b=int(input("line two:"))
    c=int(input("line three:"))
    if ((a+b)>c) & ((a+c)>b) & ((b+c)>a):
        print ("they are correct triangle side lengths\n")
    else:
        print ("they are in error\n")
