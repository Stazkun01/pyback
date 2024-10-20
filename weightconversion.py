def kg():
    mass = float(input("enter your bodyweight in kg : "))
    print(f"your bodyweight in pound is {mass * 2.205}")

def lbs():
    mass = float(input("enter your bodyweight in lbs : "))
    print(f"your bodyweight in kg is {mass / 2.205}")

print("welcome to my conversion programme !")
choice = int(input("convert from : 1- kg to lbs , 2- lbs to kg : "))
if choice == 1 :
    lbs()
elif choice == 2 :
    kg()
else :
    print("enter either 1 or 2 :")