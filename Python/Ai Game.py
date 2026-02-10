import random

# Main game loop
user_score = 0
computer_score = 0

while True:
    # Get user's choice
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            break
        print("Invalid choice. Please try again.")

    # Get computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Display choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Display result and score
    print(result)
    print("Score - You:", user_score, "Computer:", computer_score)

    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
