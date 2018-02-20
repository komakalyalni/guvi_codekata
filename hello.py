def Exploder(strin,n):
    for i in range(0,n):
        print strin
def Myfun(strin,exploder,a):
    exploder(strin,a)
Myfun("Hello",Exploder,5)