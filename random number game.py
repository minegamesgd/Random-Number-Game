import random

password = input("PASSWORD: ")
while password == "apple":
    
    randnum =  random.randrange (1,20)
    num = int(input("Choose your number (between 1 and 20)? "))
    if num == randnum:
        print("CORRECT")
    else:
        print("NOPE. TRY AGAIN!")
        
else:
    print("DENIED")
