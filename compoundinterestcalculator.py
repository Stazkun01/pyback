#Python compound interest calculator
balance = float(input(" enter the initial principal balance : "))
while balance < 0 :
    print("you broke bro why you calculating this ? ")
    balance = input(" enter a higher initial principal balance when you make some : ")
interestrate = float(input("enter the interest rate : "))
period = float(input("enter the number of time periods elapsed in years"))
n = float(input("number of time interest is copounded per year"))
final = balance*(1+ interestrate)**(n*period)
print("compoinded interest is %.2f" % final)