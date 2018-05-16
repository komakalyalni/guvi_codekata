q=int(raw_input())
n=int(raw_input())
for i in range (q,n):
    temp=i
    result=0
    while(temp!=0):
        a=temp%10
        result=result+(a**3)
        temp=temp/10
    if(result==i):
        print i
