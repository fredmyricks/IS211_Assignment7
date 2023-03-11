import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        roll = random.randint(1, 6)
        print(f"{self.name} rolled a {roll}.")
        return roll

    def take_turn(self):
        turn_score = 0
        while True:
            decision = input(f"{self.name}'s turn. Roll or hold? (r/h): ")
            if decision.lower() == "r":
                roll = self.roll_dice()
                if roll == 1:
                    print(f"{self.name} rolled a 1. Turn over.")
                    return 0
                else:
                    turn_score += roll
                    print(f"{self.name}'s turn score: {turn_score}")
            elif decision.lower() == "h":
                self.score += turn_score
                print(f"{self.name} held. Score: {self.score}")
                return turn_score

    def __str__(self):
        return f"{self.name}: {self.score}"

class Die:
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return str(self.value)

class PigGame:
    def __init__(self, num_players=2):
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.die = Die()

    def play(self):
        current_player = 0
        while all(player.score < 100 for player in self.players):
            print(f"\n{self.players[current_player]}'s turn.")
            turn_score = self.players[current_player].take_turn()
            self.players[current_player].score += turn_score
            print(f"{self.players[current_player]}'s total score: {self.players[current_player].score}\n")
            if self.players[current_player].score >= 100:
                print(f"{self.players[current_player].name} wins!")
                break
            if turn_score == 0:
                current_player = (current_player + 1) % self.num_players
            else:
                self.die.roll()
                print(f"Die value: {self.die}")
                if self.die.value == 1:
                    current_player = (current_player + 1) % self.num_players
                else:
                    continue_playing = input("Continue playing? (y/n): ")
                    if continue_playing.lower() == "n":
                        current_player = (current_player + 1) % self.num_players
                        break
                    else:
                        continue

if __name__ == "__main__":
    random.seed(0)
    num_players = int(input("Enter number of players (default is 2): ") or "2")
    game = PigGame(num_players=num_players)
    game.play()
