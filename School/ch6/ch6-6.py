n = int(input("Enter the number: "))
sum = 0
for x in range(1,n+1,1):
    sum += 1/(x**3)
print("Sum is:",sum)