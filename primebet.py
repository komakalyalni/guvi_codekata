n=int(raw_input())
q=int(raw_input())
for i in range(n,q+1):
    flag=0
    for j in range(1,i+1):
        if(i%j==0):
            flag=flag+1;
    if(flag==2):
        print i