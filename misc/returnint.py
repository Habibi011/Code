text = input("Enter the text: ")
num = ''
string = ''
for x in range(0, len(text), 1):
    if text[x] == '0' or text[x] == '1' or text[x] == '2' or text[x] == '3' or text[x] == '4' or text[x] == '5' or text[x] == '6' or text[x] == '7' or text[x] == '8' or text[x] == '9': 
        num+= text[x]
    else:
        string+= text[x]
print("The numbers are: "+num+" and the other characters are: "+string)