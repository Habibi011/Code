name = input("Enter your name: ")
gender = input("Enter your gender(M/F): ")
print("Hello","Mr "+name if gender=="M" else "Ms "+name)
match name:
    case "Man":
        print("man")