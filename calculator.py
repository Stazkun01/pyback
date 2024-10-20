firstnum = int(input("enter the first number : "))
secondnum = int(input("enter the second number : "))
operator = input("enter the operator you want to use (+ , - , * , /) : ")
if operator == "+" :
    print(firstnum + secondnum)
elif operator == "-" :
    print(firstnum - secondnum)
elif operator == "*" :
    print(firstnum * secondnum)
elif operator == "/" :
    print(firstnum / secondnum)
else :
    print("enter a valid operator")