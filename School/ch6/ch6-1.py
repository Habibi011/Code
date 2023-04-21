name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age>=18:
    print(name, "is eligible for driving license.")
else:
    print(name, "is not eligible for driving license.")


# better answer
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(name+" is eligible for driving license." if age>=18 else name+" is not eligible for driving license.")
