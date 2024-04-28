import random

print("\n         Welcome to the game ⚡︎         ")
print()

while True:   
    option = ("rock","paper","scissors")
    player = None
    
  
    while player not in option:
        player = input("enter you choice (rock , paper , scissors) :  ")
        
        
        
        
    computer_choice = random.choice(option)
    print(f"computer : {computer_choice}")
    print(f"player : {player}")

    if computer_choice=="rock" and player=="paper":
        print("congratulation you win the game ! 😎")
        
    elif computer_choice=="paper" and player=="rock":
        print("bot! win the game 🤖")
        
    elif computer_choice=="paper" and player=="scissors":
        print("coungratultion you win the game ! 😎")
        
    elif computer_choice=="scissors" and player=="paper":
        print("bot! win the game 🤖")
        
    elif computer_choice=="rock" and player == "scissors":
        print("congratulation you win the game ! 😎 ")

    elif computer_choice=="scissors" and player=="rock":
        print("bot! 🤖 win ")
    elif computer_choice == player:
        print("oops it's a tie! ")
        
    play_again = input("play again (y/n): ").lower()
    if not play_again=="y":  
        break

print("thanks for playing")