import random 

options = ("rock", "paper", "scissor")
running = True

while running:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a Tie!!")
    elif player == "Rock" and computer == "scissor": 
        print("You WIN!!")
    elif player == "Scissor" and computer == "Paper":
        print("You WIN!!")
    elif player == "Paper" and computer == "Rock":
        print("You WIN!!")
    else:
        print("YOU LOSE!!")

    play_again = input("play again (y/n): ").lower()
    if not play_again == "y":
        running = False
        
print("Thanks For Playing.")