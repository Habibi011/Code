principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
term = float(input("Enter the term: "))
num = float(input("Enter the number of times interest is compounded: "))
print("Compound interest:",principal*((1+(rate/num))**(num*term)))