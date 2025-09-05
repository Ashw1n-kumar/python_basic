def name():
    names=[]
    while True:
        n=input("enter your name:")
        if(n=="exit"):
            break
        names.append(n)    
    print(names)
    
    

name()