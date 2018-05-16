a=int(raw_input())
flag=0;
if(a<=1000):
    for i in range(1,a+1):
        if(a%i==0):
            flag=flag+1
    if(flag==2):
        print"YES"
    else:
        print"NO"
else:
    print"enter value less than 1000"
