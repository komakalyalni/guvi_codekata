n=int(raw_input())
q=int(raw_input())
if(n<=100000 and q<=100000):
    for i in range(n,q):
        if(i%2!=0):
            print i
else:
    print"values are out of range"