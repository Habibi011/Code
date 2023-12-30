ques=["Name","Roll Number","Marks"]
tup=()
counter=1
no=int(input("Enter the Number of Students: "))
print()
for i in range(no):
    subtup=()
    for x in range(3):
        ask=input("Enter "+ques[x]+" of Student "+str(counter)+": ")
        subtup+=(ask,)
    counter+=1
    print()
    tup+=(subtup,)
print(tup)
