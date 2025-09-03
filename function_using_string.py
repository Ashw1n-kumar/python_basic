#hide first two and last two numbers in mobile number
num=(input("enter the number"))
hide=num[:2]+"******"+num[-2:]
print("your number is:",hide)

#function using title
song= "party monster"
artist="weeknd"
print(f"{song.title()}-{artist.title()}")