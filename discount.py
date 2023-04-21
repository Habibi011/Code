amount = int(input("Input the amount(₹): "))
disc = int(input("Inout the discount(%): "))
print("The discount is: ₹"+ str(int((amount-(amount*(disc/100))))))