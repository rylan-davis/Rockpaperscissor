player1 = input("Player one Rock, Paper, or Scissors: ")
player2 = input("Player two Rock, Paper, or Scissors: ")

if player1 == "Rock" and player2 == "Scissors":
    print("Player one wins!")
elif player1 == "Rock" and player2 == "Paper":
    print("Player two wins!")
elif player1 == "Scissors" and player2 == "Paper":
    print("Player one wins!")
elif player1 == "Scissors" and player2 == "Rock":
    print("Player 2 wins!") 
elif player1 == "Paper" and player2 == "Scissors":
    print("Player two wins!")
elif player1 == "Paper" and player2 == "Rock":
    print("Player one wins!")
elif player1 == "Paper" and player2 == "Paper":
    print("Its a tie!")
elif player1 == "Rock" and player2 == "Rock":
    print("Its a tie!")
elif player1 == "Scissors" and player2 == "Scissors":
    print("Its a tie!")        
else:
    print("You did not enter correctly")