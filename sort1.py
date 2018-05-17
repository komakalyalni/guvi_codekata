try:
    n=input()
    a=[]
    if(1<=n<=1000):
        for i in range(0,n):
            n1=input()
            list.append(n1)
        print list
        list.sort()
        print"sorted list is",list
    else:
        print"Invalid Input"
except:
    print"Invalid Input"