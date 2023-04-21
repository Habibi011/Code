text = input("Enter the text: ")
output =''
for x in range(0,len(text),1):
    output += text[x]+text[x]
print("doubled letters is: ", output)
