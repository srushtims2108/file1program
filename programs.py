#1. swap first and last options in a list

names = [ "john" , "abhay" , "shreya" , "mohan" , "navya"]
names[0] = "navya"
names[4] = "john"
print(names)

#2. swap first and last options in a list

def swap(names):
    temp = names[0]
    names[0] = names[len(names) - 1]
    names[len(names) - 1] = temp
    return names

names = [ "john" , "abhay" , "shreya" , "mohan" , "navya"]

print(swap(names))

#check if a string is palindrome or not

str = "srushti"

def palindrome(str):
    return str == str[::-1]

print(palindrome(str))