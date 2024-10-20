# 1. username is not more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("enter a username : ")
while username == "":
    print("you did not enter your username ! ")
    username = input("enter a valid username : ")
while len(username) > 12 :
    print("your username cannot contain more than 12 characters") 
    username = input("enter a valid username : ")
while username.find(" ") > -1 :
    print("your username cannot contain spaces ")
    username = input("enter a valid username : ")
while username.isalpha() == False:
    print("your username cannot contain digits ")
    username = input("enter a valid username : ") 
print(f"welcome {username}")