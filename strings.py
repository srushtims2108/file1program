print("hey!! welcome to the quiz game")
x = input("would you like to start the quiz")
if x == "yes":
    print("lessgo!!")
else:
    print("try again")
    quit()

print("answer the given questions below")

score = 0
print("ur score is zero")

q1 = input("whats the sum of 1 and 3") 
if q1 == "4":
    print("correct answer")
    score+=1
else:
    print("your answer is incorrect")

q2 = input("whats the product of 2 and 3") 
if q2 == "6":
    print("correct answer")
    score+=1
else:
    print("your answer is incorrect")

q3 = input("whats the difference of 6 and 3") 
if q3 == "3":
    print("correct answer")
    score+=1
else:
    print("your answer is incorrect")

q4 = input("whats the sum of 5 and 3") 
if q4 == "8":
    print("correct answer")
    score+=1
else:
    print("your answer is incorrect")

print("your total score is ", score)





