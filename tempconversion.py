def k():
    temp = float(input("enter your temperature in C : "))
    print(f"your temperature in kelvin is equale to {temp + 273,15}")
def C():
    temp = float(input("enter your temperature in k : "))
    print(f"your temperature in Celcius is equale to {temp - 273,15}")

choice = int(input("convert from : 1- Kelvin to Celcius . 2- Celcuis to Kelvin  "))
if choice == 1 :
    C()
elif choice == 2 :
    k()
else : 
    print("enter a valid choice : ")
