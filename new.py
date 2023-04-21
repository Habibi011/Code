import math
y=0
num1= input("Input the decimal: ")
z= int(num1.replace('.', ''))
for x in num1:
    if x == '.':
        y+=1
den = 10**((len(num1)-(y+1)))
hcf = math.gcd(z,den)
print("Your fraction is: ",int(z/hcf), "/", int(den/hcf))
