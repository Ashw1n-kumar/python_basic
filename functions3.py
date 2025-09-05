def name():
    name=[]
    howmuch=int(input("enter how much do you want:"))
    for i in range(howmuch):
        i=input("enter your name:")
        name.append(i)
    print(name)
name()