def calci():
    a=int(input("enter the value a:"))
    b=int(input("enter the value b:"))
    c=input("enter the operation:")
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        print(a/b)
    
def tables():
    mul=int(input("enter the value of mulitipeer:"))
    upto=int(input("enter the value upto:"))
    for i in range (1,upto+1):
        print(mul,"@",i,"=",mul*i)

def main():
    print("what function do you want:for table press 1,for calci press 2:")
    print("**************************************************************")
    get=int(input("enter the number you want:"))
    if (get==1):
        tables()
        main()
    elif (get==2):
        calci()
        main()
    else:
        print("invalid")
        main()
main()