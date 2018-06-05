#Neomi Mayer 328772801

def middles(a,b,c,d):
    midlist=[0]*4
    if b>a :
        midlist = [a,b]
    else: midlist = [b,a]
    if c<midlist[0]:
        midlist.append(midlist[1])
        midlist[1] = midlist[0]
        midlist[0] = c
    elif c<midlist[1]:
          midlist.append(midlist[1])
          midlist[1] = c
    else: midlist.append(c)
    if d<midlist[0]:
        midlist.append(midlist[2])
        midlist[2] = midlist[1]
        midlist[1] = midlist[0]
        midlist[0]=d
    elif d<midlist[1]:
         midlist.append(midlist[2])
         midlist[2]=midlist[1]
         midlist[1]=d
    elif d<midlist[2]:
         midlist.append(midlist[2])
         midlist[2]=d
    else: midlist.append(d)
    return midlist
    
    
    
    

while True:
    print("enter four numbers: \n")
    a=int(input("first: "))
    b=int(input("second: "))
    c=int(input("third: "))
    d=int(input("fourth: "))
    mid = middles(a,b,c,d)
    print(mid[1]," ",mid[2],"\n")
    
