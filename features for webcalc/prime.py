ask = input("Do you want to start?(y/n)")
while ask=='y':
    num = int(input("Enter the number(non-negative): "))
    status =0
    for x in range(2,int(num**(1/2))+1,1):
        if num%x == 0:
            status = 1
            break
    print(num, "is neither prime nor composite" if num==1 or num==0 else "is composite" if status==1 else "is prime")
    ask = input("Do you want to start again?(y/n)")

    
            
