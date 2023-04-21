num = input("Enter your number: ")
check = ""
for x in range(len(num)-1,-1,-1):
    check+= num[x]
print(num+" is a palindrome." if check==num else num+" is not a palindrome")