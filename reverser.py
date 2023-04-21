text = input("Enter your word to be reversed: ")
output = ''
for x in range(len(text)-1,-1, -1):
    output += text[x]
print(output)