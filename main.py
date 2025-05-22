import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter rock, paper, or scissors: ").lower()
        if user_input in choices:
            return user_input
        print("Invalid choice. Try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
