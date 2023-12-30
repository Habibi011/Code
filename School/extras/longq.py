n=int(input("How many friends? "))
fd={}
for i in range(n):
    print("Enter details of a friend",(i+1))
    name=input("Name: ")
    ph=int(input("Phone: "))
    fd[name]=ph
    print("Friends dictionary is",fd)
ch=0
while ch!=7:
    print("\tMenu")
    print("1. Display all friends")
    print("2. Add new friend")
    print("3. Delete a friend")
    print("4. Modify a phone number")
    print("5. Search for a friend")
    print("6. Sort on names")
    print("7. Exit")
    ch=int(input("Enter the choice (1..7): "))
    if ch==1:
        print(fd)
    elif ch==2:
        print("Enter the details of new friend")
        name=input("Name: ")
        ph=int(input("Phone: "))
        fd[name]=ph
    elif ch==3:
        nm=input("Friend name to be deleted: ")
        res=fd.pop(nm,-1)
        if res!=-1:
            print(res,"deleted")
        else:
            print("No such friend")
    elif ch==4:
        name=input("Friend Name: ")
        ph=int(input("Changed phone: "))
        fd[name] = ph
    elif ch ==5:
        name=input("Friend Name: ")
        if name in fd:
            print(name,"exists in the dictionary.")
        else:
            print(name,"does not exists in the dictionary.")
    elif ch==6:
        lst=sorted(fd)
        print("{",end=" ")
        for a in lst:
            print(a,":",fd[a],end=" ")
        print("}")
    elif ch==7:
        break
    else:
        print("Valid choices are 1..7")