num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num1>=num2 and num1>=num3:
    if num2>num3:
        print("Largest number: ", num1,"Smallest number: ", num3)
    else:
        print("Largest number: ", num1,"Smallest number: ", num2)
elif num3>=num2 and num3>=num2:
    if num1>num2: 
        print("Largest number: ", num3,"Smallest number: ", num2)
    else:
        print("Largest number: ", num3,"Smallest number: ", num1)
else:
    if num3>num1: 
        print("Largest number: ", num2,"Smallest number: ", num1)
    else:
        print("Largest number: ", num2,"Smallest number: ", num3)

