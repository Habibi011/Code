import time
import os
import sys
word=""
totalAttempts=6
display=[]
wordList=[]
guessList=[]
guess=""
def load():
   loadText="loading"
   for x in range(1,5):
      time.sleep(0.1)
      print(loadText, end="\r")
      loadText+="."
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
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
def askWord():
  global word
  print("Enter the word which your friend can guess")
  word=input("(Make sure they are not looking): ").lower()
  print()
  load()
  clearScreen()
  wordAlpha= word.isalpha()
  if not wordAlpha:
      print("ERROR !! Invalid word! Only alphabets allowed! Change the word.")
      print("")
      print("------------------------------------------------------------------------")
      print("")
      askWord()
def ask():
     global guessList
     global guess
     global totalAttempts
     global display
     guess= (input("Enter your guess: ")).lower()
     clearScreen()
     print("You entered:", guess)
     load()
     sys.stdout.write('\x1b[2K') 
     alpha=guess.isalpha()
     if not alpha:
        print("")
        print("!! Only Alphabets are allowed !!")
        print("")
        print("No. of incorrect attempts left:",totalAttempts)
        if guessList != []:
            print("")
            print("Words used till now:"," , ".join(guessList))
        print("----------------------------------------")
        print("")
        drawMan(totalAttempts)
        print(" ".join(display))
        print("")
        ask()
     elif len(guess)>1:
        print("")
        print("!! Please Enter Only One Character at a time !!")
        print("")
        print("No. of incorrect attempts left:",totalAttempts)
        if guessList != []:
            print("")
            print("Words used till now:"," , ".join(guessList))
        print("")
        print("----------------------------------------")
        print("")
        drawMan(totalAttempts)
        print(" ".join(display))
        print("")
        ask()
     elif guess in guessList:
         print("")
         print("This letter was already used. Other letters used:- ")
         print("")
         print(" , ".join(guessList))
         print("")
         print("No. of incorrect attempts left:",totalAttempts)
         print("")
         print("----------------------------------------")
         print("")
         drawMan(totalAttempts)
         print(" ".join(display))
         print("")
         ask()
     else:
         guessList.append(guess)
def retry():
   print("")
   global guessList
   ask=input("Do you want to start again?(y/n): ")
   print()
   load()
   if ask=='y':
      guessList=[]
      clearScreen()
      main()
   elif ask == 'n':
      clearScreen()
      print("!! 🎮 HANGMAN 🎮 !!")
      print("")
      print("Thanks for playing!")
      quit()
   else:
      clearScreen()
      print("Please enter (y/n) only")
      retry()
def main():
   global word
   global totalAttempts
   global display
   global wordList
   global guess
   global guessList  
   totalAttempts=6
   display=[]
   wordList=[]
   guess=""
   print("!! 🎮 HANGMAN 🎮 !!")
   print("")
   askWord()
   print("!! 🎮 HANGMAN 🎮 !!")
   print("")
   print("Rules:- 1) Enter characters from a-z.")
   print("        2) You have 6 wrong attempts, Game over at 0.")
   print("        3) Figure out the word, making less than 6 mistakes to win.")
   print("        4) Please enter only one character at a time.")
   print("")
   input("Press enter to continue: ")
   print()
   load()
   clearScreen()
   for x in range(0,len(word),1):
      wordList.append(word[x])
      display.append("_")

   drawMan(totalAttempts)
   print(" ".join(display))
   print("")
   print("No. of incorrect attempts left:",totalAttempts)
   print("")


   while display!=wordList and totalAttempts!=0: 
      ask()
      if guess in wordList:
         time.sleep(0.5)  
         print("")
         print("✅ Right Guess ✅")
         for x in range(0,len(word),1):
               if guess == wordList[x]:
                     display[x]=guess  
      else:
         totalAttempts-=1
         time.sleep(0.5)
         print("")
         print("❌ Wrong guess ❌")
      print("")
      print("No. of incorrect attempts left:",totalAttempts)
      print("")
      print("Words used till now:"," , ".join(guessList))
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      print("")
      drawMan(totalAttempts)
      print(" ".join(display))
      print("")

   if totalAttempts!=0:
      time.sleep(0.5)
      print("! 🎊 YOU WON 🎊 !")
      print("")
      print("The word was:",word)
   else:
      time.sleep(0.5)
      print("! 😥 YOU LOST 😥 !")
      print("")
      print("The word was:",word)
   retry()
main()