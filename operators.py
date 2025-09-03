print("sample of opertaion press 1,waht to do sample 2 press 2")
one=int(input("enter the number"))
if (one==1):
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    #arithmatic opertors
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a**b) #power
    print(a//b) #if decimal give the grater value from float

    #comparison
    print(a==b)
    print(a!=b)
    print(a<b)
    print(a>b)

    #logical
    x=True
    y=False
    print(x and y)
    print(x or y)
    print(not x)
elif(one==2):#sample program with salary and discount,gst
    xx=int(input("enter the salary"))
    gst=xx*0.18
    print("gst for your amount:",gst)
    total=xx+gst
    dis=total*0.10
    h=total-dis
    print("discount:",dis,"after discount is",h)
