ask = input("Do you want to start? (y/n): ")
while ask == "y":
    text = input("Enter the word or sentence: ")
    vowel = 0
    cons = 0
    for x in range(0, len(text), 1):
        if text[x]=='a' or text[x]=='e'or text[x]=='i' or text[x]=='o' or text[x]=='u' :
            vowel+=1
        else:
            cons+=1
    print("There are ",vowel, " vowels and ", cons," consonants")
    ask = input("Do you want to start again? (y/n): ")