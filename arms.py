n=int(raw_input());
temp=n
result=0
while(temp!=0):
    a=temp%10
    result=result+(a**3)
    temp=temp/10
if(result==n):
    print"yes"
else:
    print"no"
