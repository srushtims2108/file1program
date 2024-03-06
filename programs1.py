#interchange two numbers in a list

list = [ 1 , 2, 4 ,3 , 6 , 5]

x = input("enter the  first index of list to be swapped ")
y = input("enter the  second index of list to be swapped ")


def swap(list):
    temp = list[int(x)]
    list[int(x)] = list[int(y)]
    list[int(y)] = temp
    return list

print(swap(list))





    