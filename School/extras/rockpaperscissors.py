import random
import time
scoreComputer = 0
scorePlayer= 0
roundNum = 0

print("ROCK PAPER SCISSORS!")
time.sleep(1)
print(" ")
totalRounds = int(input(("Enter the number of rounds you want to play: ")))
def game():
    global scoreComputer
    global scorePlayer
    global roundNum
    global totalRounds

    if roundNum !=totalRounds:
        time.sleep(1)
        print("ROUND",roundNum+1)
        print(" ")
        playerChoice = input("Enter your choice; Rock(r), Paper(p), Scissors(s): ")
        print("YOU CHOSE: ",("ROCK" if playerChoice == 'r' else "PAPER" if playerChoice == 'p' else "SCISSORS"))
        time.sleep(1)
        print(" ")
        computerChoice = random.randint(0,2)
        print("COMPUTER CHOOSES:",("ROCK" if computerChoice == 0 else "PAPER" if computerChoice == 1 else "SCISSORS"))
        time.sleep(1)
        print(" ")
        match(playerChoice):
            case 'r':
                match(computerChoice):
                    case 0:
                        print("IT\'S A TIE")
                        scoreComputer+=1
                        scorePlayer+=1
                    case 1:
                        print("COMPUTER WON THE ROUND")
                        scoreComputer+=1
                    case 2:
                        print("YOU WON THE ROUND")
                        scorePlayer+=1
            case 'p':
                match(computerChoice):
                    case 0:
                        print("YOU WON THE ROUND")
                        scorePlayer+=1
                    case 1:
                        print("IT\'S A TIE")
                        scoreComputer+=1
                        scorePlayer+=1
                    case 2:
                        print("COMPUTER WON THE ROUND")
                        scoreComputer+=1
            case 's':
                match(computerChoice):
                    case 0:
                        print("COMPUTER WON THE ROUND")
                        scoreComputer+=1
                    case 1:
                        print("YOU WON THE ROUND")
                        scorePlayer+=1
                    case 2:
                        print("IT\'S A TIE")
                        scoreComputer+=1
                        scorePlayer+=1
        roundNum+=1
        print("Your score:",scorePlayer,"  Computer\'s score:",scoreComputer) if roundNum!=totalRounds else ""
        game()
    else:
        print(" ")
        print("GAME COMPLETED!")
        print(" ")
        print("YOUR SCORE WAS:", scorePlayer)
        print("COMPUTER\'S SCORE WAS:",scoreComputer)
        print(" ")
        print("!! COMPUTER WON !!" if scoreComputer>scorePlayer else "!! YOU WON !!" if scoreComputer<scorePlayer else "!! I\'S A TIE !!")
game()   