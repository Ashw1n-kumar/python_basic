#L #E #G #B
#create a varible with #l local variable
def order():
    food="rice"
    print("your order is",food)
order()
#but if we call food out side the class it wouldn't show the value

#E (enclosing)
#the function may used inside the function
def cart():
    discount=10
    def cheakout():
        print("your discount value is:",discount)
    cheakout()
cart()

#G global variable 
#varible must be in out side the function
name="ashwin"
def home():
    print("your name is ",name)
def profile():
    new_var = print("your profile name is ",name)
    new_var
home()
profile()

#B built in variable
#for example
py=__file__
print(py)