import random


class Player:
    """Class representing a player in the game."""
    def __init__(self, name):
        self.name = name
        self.total_score = 0

    def add_score(self, score):
        """Add score to the player's total."""
        self.total_score += score

    def reset(self):
        """Reset the player's total score."""
        self.total_score = 0


class PigGame:
    """Class representing the Pig game."""
    def __init__(self, target_score=100):
        self.target_score = target_score
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player_index = 0
        self.current_turn_score = 0

    def roll_die(self):
        """Simulate rolling a 6-sided die."""
        return random.randint(1, 6)

    def switch_player(self):
        """Switch to the next player."""
        self.current_player_index = 1 - self.current_player_index
        self.current_turn_score = 0

    def current_player(self):
        """Return the current player."""
        return self.players[self.current_player_index]

    def take_turn(self):
        """Handle the current player's turn."""
        print(f"\n{self.current_player().name}'s turn.")
        while True:
            print(f"Total score: {self.current_player().total_score}")
            print(f"Turn score: {self.current_turn_score}")
            choice = input("Roll or Hold? (r/h): ").lower()

            if choice == 'r':
                roll = self.roll_die()
                print(f"You rolled: {roll}")
                if roll == 1:
                    print("Rolled a 1! No points this turn.")
                    self.switch_player()
                    break
                else:
                    self.current_turn_score += roll
            elif choice == 'h':
                self.current_player().add_score(self.current_turn_score)
                print(f"{self.current_player().name} holds with {self.current_player().total_score} points.")
                if self.current_player().total_score >= self.target_score:
                    return True
                self.switch_player()
                break
            else:
                print("Invalid choice! Please choose 'r' to roll or 'h' to hold.")
        return False

    def play(self):
        """Start the game loop."""
        print("Welcome to Pig!")
        print(f"First to reach {self.target_score} points wins.\n")
        while True:
            if self.take_turn():
                print(f"\n{self.current_player().name} wins with {self.current_player().total_score} points!")
                break
        print("Game Over.")


if __name__ == "__main__":
    # Initialize and play the game
    pig_game = PigGame(target_score=100)
    pig_game.play()