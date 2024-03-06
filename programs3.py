import random
import string

characters = string.ascii_letters + string.digits + "!@#$%^&*"

A1  = input("do u wanna generate a password?? : ")

if A1 == "yes":
    print("Here we gooo!!!")
elif A1 == "no":
    print("okay!! thank you for ur interest")
    quit()    
else:
    print("invalid input!! try again")
    quit()
   
l = input("enter the length of password: ")
l1 = int(l)

password = []

for x in range(l1):
    password.append(random.choice(characters))

password = "".join(password)
print(password)