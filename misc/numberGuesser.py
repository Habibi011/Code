import time
import os
import sys
import random
ask=None
num=0
counter=0
Max=100
Min=0
x=0
def load():
   loadText="loading"
   for x in range(1,5):
      time.sleep(0.1)
      print(loadText, end="\r")
      loadText+="."
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
def clearLine():
   sys.stdout.write('\x1b[2K')
def askNum():
   global ask
   ask=input("Enter your guess(1-100): ")
   print()
   load()
   clearScreen()
   checkNum= ask.isnumeric()
   if not checkNum:
        print("ERROR !! Invalid number! Only integers allowed!")
        print("")
        print("------------------------------------------------------------------------")
        print("")
        askNum()
   else:
      ask = int(ask)
def retry():
   print("")
   global num
   global counter
   global Max
   global Min
   Max=100
   Min=0
   counter=0
   ask=input("Do you want to start again?(y/n): ")
   print()
   load()
   if ask=='y':
      num=random.randint(1,100)
      counter=0
      clearScreen()
      print("!! 🎮 GUESS THE NUMBER 🎮 !!")
      print("")
      print("Guess the number between 1 and 100!")
      print()
      input("Press enter to continue")
      load()
      clearScreen()
      main()
   elif ask == 'n':
      clearScreen()
      print("!! 🎮 GUESS THE NUMBER 🎮 !!")
      print("")
      print("Thanks for playing!")
      quit()
   else:
      clearScreen()
      print("Please enter (y/n) only: ")
      retry()
def main():
   global ask
   global counter
   global Max
   global Min
   if counter!=0:
      print()
      print("The number lies between",Min,"and",Max)
      print()
   askNum()
   load()
   clearScreen()
   if ask>num:
      print("Guess lower, Current Guess: ", ask)
      if ask<Max:
          Max=ask
      counter+=1
      main()
   elif ask<num:
      print("Guess Higher, Current Guess: ",ask)
      if ask>Min:
          Min=ask
      counter+=1
      main()
   elif ask==num:
      print("You guessed the number!:",num)
      print("No. of Attempts: ",counter)
      retry()
   else:
      print("Error")
      main()
   x+=1

   
num=random.randint(1,100)
print("!! 🎮 GUESS THE NUMBER 🎮 !!")
print("")
print("Guess the number between 1 and 100!")
input("Press enter to continue")
load()
clearScreen()
main()