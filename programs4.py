import math
n = input("enter the value : ")
n1 = int(n)

if n1%2==1:
    print("weird")
elif n1%2==0 and 2<=n1<=5:
    print("not weird")
elif n1%2==0 and 6<=n1<=20:
     print("weird")
elif n1%2==0 and 20<=n1<=100:
    print("not weird")
else:
    quit()