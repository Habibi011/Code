#type converter
num = input("Enter the number (decimal): ")
print("Select the data type in which you want to convert the Number: ")
datatype = input("Binary(b), Octal(o), Hex(h), decimal(d): ")
match num[1]:
    case 'b':
        init = bin(num)
        match datatype:
            case 'd':
                print(int(num))
            case 'o':
                print(oct(num))
            case 'h':
                print(hex(num))
    case 'o':
        init = oct(num)
        match datatype:
            case 'b':
                print(bin(num))
            case 'd':
                print(int(num))
            case 'h':
                print(hex(num))
    case 'x':
        init = hex(num)
        match datatype:
            case 'b':
                print(bin(num))
            case 'o':
                print(oct(num))
            case 'd':
                print(int(num))
    case _:
        match datatype:
            case 'b':
                print(bin(num))
            case 'o':
                print(oct(num))
            case 'h':
                print(hex(num))

