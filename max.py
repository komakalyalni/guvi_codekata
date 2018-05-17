n=input()
list=[]
if(1<=n<=1000):
    for i in range(0,n):
        n1=input()
        list.append(n1)
    print list
    print (max(list))
else:
    print"Invalid Input"