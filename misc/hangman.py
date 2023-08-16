import time
word=("Hangman").lower()
def drawMan(x):
   match x:
      case 6:
         print("  |------|")
         print("         |")
         print("         |")
         print("         |")
         print("         |")
         print(" ==========")
      case 5:
         print("  |------|")
         print("  O      |")
         print("         |")
         print("         |")
         print("         |")
         print(" ==========")
      case 4:
         print("  |------|")
         print("  O      |")
         print("  |      |")
         print("         |")
         print("         |")
         print(" ==========")
      case 3:
         print("  |------|")
         print("  O      |")
         print(" /|      |")
         print("         |")
         print("         |")
         print(" ==========")
      case 2:
         print("  |------|")
         print("  O      |")
         print(" /|\     |")
         print("         |")
         print("         |")
         print(" ==========")
      case 1:
         print("  |------|")
         print("  O      |")
         print(" /|\     |")
         print(" /       |")
         print("         |")
         print(" ==========")
      case 0:
         print("  |------|")
         print("  0      |")
         print(" /|\     |")
         print(" / \     |")
         print("         |")
         print(" ==========")

print("")
print("!! 🎮 HANGMAN 🎮 !!")
print("")
print("Rules:- 1) Enter characters from a-z.")
print("        2) You have 6 wrong attempts, Game over at 0.")
print("        3) Figure out the word, making less than 6 mistakes to win.")
print("        4) Please enter only one character at a time.")
print("        5) Change the word inside double quotes (\" \") in the 2nd line")
print("           of this code to play multiple games among friends!")
print("")
wordAlpha= word.isalpha()
if not wordAlpha:
   print(" ERROR !! Invalid word! Only alphabets allowed! Change word and restart program.")
   quit()
print("------------------------------------------------------------------------")
print("")

totalAttempts=6
display=[]
wordList=[]
guess=""

for x in range(0,len(word),1):
   wordList.append(word[x])
   display.append("_")

drawMan(totalAttempts)
print(" ".join(display))
print("")
print("No. of incorrect attempts left:",totalAttempts)
print("")

def ask():
     global guess
     guess= (input("Enter your guess: ")).lower()
     alpha=guess.isalpha()
     if not alpha:
        print("")
        print("!! Only Alphabets are allowed !!")
        print("----------------------------------------")
        print("")
        drawMan(totalAttempts)
        print(" ".join(display))
        print("")
        ask()
     elif len(guess)>1:
        print("")
        print("!! Please Enter Only One Character at a time !!")
        print("----------------------------------------")
        print("")
        drawMan(totalAttempts)
        print(" ".join(display))
        print("")
        ask()
while display!=wordList and totalAttempts!=0: 
    ask()
    if guess in wordList:
     time.sleep(0.5)  
     print("")
     print(" ✅ Right Guess ✅ ")

     for x in range(0,len(word),1):

        if guess == wordList[x]:
            display[x]=guess  
    else:
     totalAttempts-=1
     time.sleep(0.5)
     print("")
     print(" ❌ Wrong guess ❌ ")
    
    print("")
    print("No. of incorrect attempts left:",totalAttempts)
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    drawMan(totalAttempts)
    print(" ".join(display))
    print("")

if totalAttempts!=0:
   time.sleep(0.5)
   print("! 🎊 YOU WON 🎊 !")
   print("")
   print("No. of incorrect attempts left:",totalAttempts)
else:
   time.sleep(0.5)
   print("! 😥 YOU LOST 😥 !")
   print("")
   print("No. of incorrect attempts left:",totalAttempts)
   print("")
   print("The word was:",word)
