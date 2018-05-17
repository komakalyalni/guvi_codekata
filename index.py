try:
    n=int(raw_input())
    a=[]
    for i in range(1,n+1):
        n1=int(raw_input())
        a.append(n1)
    for i in range(0,n):
        print a[i],i
except:
    print"invalid"