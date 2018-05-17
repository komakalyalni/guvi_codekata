try:
    n=int(raw_input())
    a=int(raw_input())
    d=int(raw_input())
    if(1<=n and a and d <=100000):
        currentvalue=a
        su=a
        for i in range (1,n):
            currentvalue=currentvalue+d
            su=su+currentvalue
        print su
    else:
        print"invalid"
except:
    print"invalid"