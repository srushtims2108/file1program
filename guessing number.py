x = int(input("enter the number to be guessed: "))

t= int(input(" enter the number of guesses : "))

def guess():
    guess = int(input("guess the number: "))

    if guess==x:
        print("you guessed it right!!")
        quit()
    else:
        print("try again")
 
i=0

while(i<t):
    i+=1
    guess()
