print("Welcome to Stone,Paper,Scissor game")
import random
computer_choice=random.randint(1,3)
print("===== Rules =====")
print(" 1 = Stone")
print(" 2 = Paper")
print(" 3 = Scissor")
print("===== Rules =====")
while True:
    choice=int(input("Enter your choice:"))
    print(f"Computer's choice is :{computer_choice}")
    if choice ==1 and computer_choice==1:
        print("Its Draw cause both choice is same")
    elif choice == 2 and computer_choice == 2:
        print("Its Draw cause both choice is same")
    elif choice == 3 and computer_choice == 3:
        print("Its Draw cause both choice is same")
    elif choice == 1 and computer_choice == 2:
        print("You Lose cause Paper Wraps Stone..")
    elif choice == 2 and computer_choice == 1:
        print("You won cause Paper Wraps Stone..")
    elif choice == 3 and computer_choice == 2:
        print("You Won cause Scissor cuts The Paper..")
    elif choice == 2 and computer_choice == 3:
        print("You lose cause Scissors cuts The Paper..")
    elif choice == 1 and computer_choice == 3:
        print("You won cause stone brokes The Scissors..")
    elif choice == 3 and computer_choice == 1:
        print("You lose cause stone brokes The Scissors..")
    txt=input("do you want to continue Y or N:")
    if txt=="Y" or txt=="y":
        print("Then play the game..")
    elif txt=="N" or txt=="n":
        break
    else:
        print("Invalid choice enter appropriate answer..")