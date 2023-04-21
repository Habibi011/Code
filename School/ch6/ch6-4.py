year = int(input("Enter a year: "))
if year%4==0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# better answer
# year = int(input("Enter a year: "))
# print(str(year)+" is a leap year" if year%4==0 else str(year)+" is not a leap year")