a = int(input("Enter coefficient of x²: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter constant: "))
D = (b**2)-4*a*c
print("There are 2 unequal real roots." if D>0 else "There are 2 equal roots" if D==0 else "There are no real roots")