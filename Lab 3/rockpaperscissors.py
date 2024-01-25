import random

class RPSBot:
    def __init__(self):
        self.state_machine = {
            'rock': {'rock': 'draw', 'paper': 'lose', 'scissors': 'win'},
            'paper': {'rock': 'win', 'paper': 'draw', 'scissors': 'lose'},
            'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'draw'}
        }
        self.user_score = 0
        self.bot_score = 0

    def get_user_choice(self):
        valid_choices = ['rock', 'paper', 'scissors']
        while True:
            user_input = input("Enter your choice (rock/paper/scissors): ").lower()
            if user_input in valid_choices:
                return user_input
            else:
                print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_bot_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def play_round(self, user_choice, bot_choice):
        result = self.state_machine[user_choice][bot_choice]

        if result == 'win':
            self.user_score += 1
            print(f"You win! {user_choice.capitalize()} beats {bot_choice}.")
        elif result == 'lose':
            self.bot_score += 1
            print(f"You lose! {bot_choice.capitalize()} beats {user_choice}.")
        else:
            print(f"It's a draw! Both chose {user_choice}.")

        print(f"Score: User {self.user_score} - {self.bot_score} Bot\n")

    def play_game(self):
        while True:
            user_choice = self.get_user_choice()
            bot_choice = self.get_bot_choice()
            self.play_round(user_choice, bot_choice)

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    rps_bot = RPSBot()
    rps_bot.play_game()
