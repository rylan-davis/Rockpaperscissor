import random

list1 = ["Rock", "Paper", "Scissors"]
player = input("Rock, Paper, or Scissors?: ")
bot = random.choice(list1)


if player == "Rock" and bot == "Scissors" or player == "Scissors" and bot == "Paper" or player == "Paper" and bot == "Rock":
    print("Bot chose", bot, " and you win!")
elif player == "Rock" and bot == "Paper" or player == "Scissors" and bot == "Rock" or player == "Paper" and bot == "Scissors":
    print("Bot chose", bot , "and wins!")
elif player == "Rock" and bot == "Rock" or player == "Scissors" and bot == "Scissors" or player == "Paper" and bot == "Paper":
    print("Its a tie!")
else:
    print("Something went wrong!")


"""
if player == "Rock":
    if bot == "Scissors":
        print("You win!")
    elif bot == "Paper":
        print("Bot wins!")
    else:
        print("Its a tie!")
elif player == "Paper":
    if bot == "Rock":
        print("You win!")
    elif bot == "Scissors":
        print("Bot wins!")
    else:
        print("Its a tie!")
elif player == "Scissors":
    if bot == "Paper":
        print("You win!")
    elif bot == "Rock":
        print("Bot wins!")
    else:
        print("Its a tie!")
else:
    print("Something went wrong!")

    

if player == "Rock" and bot == "Scissors":
    print("You win!")
elif player == "Rock" and bot == "Paper":
    print("bot wins!")
elif player == "Scissors" and bot == "Paper":
    print("You win!")
elif player == "Scissors" and bot == "Rock":
    print("bot wins!") 
elif player == "Paper" and bot == "Scissors":
    print("bot wins!")
elif player == "Paper" and bot == "Rock":
    print("You win!")
elif player == "Paper" and bot == "Paper":
    print("Its a tie!")
elif player == "Rock" and bot == "Rock":
    print("Its a tie!")
elif player == "Scissors" and bot == "Scissors":
    print("Its a tie!")        
else:
    print("You did not enter correctly")

"""