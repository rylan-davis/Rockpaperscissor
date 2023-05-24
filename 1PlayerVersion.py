import random

list1 = ["Rock", "Paper", "Scissors"]
player = input("Rock, Paper, or Scissors?: ")
bot = random.choice(list1)


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

# Better looking code /\
# Less good looking code \/
"""
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