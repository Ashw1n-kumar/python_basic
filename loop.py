#find the number is odd or even or exit
a=""
while a!="exit":
    if a=="exit":
        break
    a=int((input("enter the number:")))

    if (a%2==0):
        print("it is even")
    else:
        print("odd")
print("program ended")